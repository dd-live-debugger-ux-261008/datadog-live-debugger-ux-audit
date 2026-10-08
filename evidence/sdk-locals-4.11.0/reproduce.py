"""Offline reproduction using actual installed SDK helpers; no Agent or application runtime."""
import hashlib
import importlib.metadata
import json
from pathlib import Path
import sys

blocked_network_attempts = 0


def deny_network(event, args):
    global blocked_network_attempts
    if (event.startswith("socket.") and event != "socket.gethostname") or event in ("subprocess.Popen", "os.system"):
        blocked_network_attempts += 1
        raise RuntimeError("external execution disabled in offline SDK reproduction")


sys.addaudithook(deny_network)

from ddtrace.debugging._safety import get_locals
from ddtrace.debugging._signal.utils import capture_pairs, capture_value
from ddtrace.debugging._expressions import DDExpression


def observe(assign_optional=False):
    assigned = 42
    explicit_none = None
    if assign_optional:
        unbound = 99
    deleted = 101
    del deleted
    frame = sys._getframe()
    native = dict(frame.f_locals)
    sdk = dict(get_locals(frame))
    names = ("assigned", "explicit_none", "unbound", "deleted")
    captured = capture_pairs((name, sdk[name]) for name in names)
    return {name: {
        "present_in_frame_locals": name in native,
        "sdk_local_is_none": sdk[name] is None,
        "sdk_isDefined": DDExpression.compile({"dsl": "isDefined(" + name + ")", "json": {"isDefined": {"ref": name}}}).eval(native),
        "sdk_serialized": captured[name],
    } for name in names}


result = {
    "package": "ddtrace", "version": importlib.metadata.version("ddtrace"),
    "python_version": sys.version.split()[0],
    "helper_source_sha256": {
        str(Path(fn.__code__.co_filename).name): hashlib.sha256(Path(fn.__code__.co_filename).read_bytes()).hexdigest()
        for fn in (get_locals, capture_value)
    },
    "unassigned_control": observe(False), "assigned_control": observe(True),
}
assert result["version"] == "4.11.0"
assert result["unassigned_control"]["assigned"]["sdk_serialized"] == {"type": "int", "value": "42"}
for name in ("unbound", "deleted"):
    row = result["unassigned_control"][name]
    assert row["present_in_frame_locals"] is False and row["sdk_isDefined"] is False
    assert row["sdk_serialized"] == {"type": "NoneType", "isNull": True}
assert result["unassigned_control"]["explicit_none"]["present_in_frame_locals"] is True
assert result["unassigned_control"]["explicit_none"]["sdk_isDefined"] is True
assert result["assigned_control"]["unbound"]["sdk_serialized"] == {"type": "int", "value": "99"}
result["blocked_network_or_subprocess_attempts"] = blocked_network_attempts
result["scope"] = "Actual SDK helper calls only; socket/subprocess audit guard installed before SDK import; SDK telemetry/tracing/RC disabled in clean environment. No hosted capture payload inspected."
print(json.dumps(result, indent=2))
