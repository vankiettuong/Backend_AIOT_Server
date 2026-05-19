from datetime import datetime, timezone
from typing import Optional, Tuple
import math

UTC = timezone.utc


def utc_now() -> datetime:
    return datetime.now(tz=UTC)


def parse_ts(value: Optional[str]) -> datetime:
    if not value:
        return utc_now()
    dt = datetime.fromisoformat(value.replace("Z", "+00:00"))
    if dt.tzinfo is None:
        dt = dt.replace(tzinfo=UTC)
    return dt.astimezone(UTC)


def floor_time(dt: datetime, interval_seconds: int) -> datetime:
    epoch = int(dt.timestamp())
    floored = epoch - (epoch % interval_seconds)
    return datetime.fromtimestamp(floored, tz=UTC)


def cyclic_hour_features(dt: datetime) -> Tuple[float, float]:
    hour = dt.hour + dt.minute / 60.0
    angle = 2.0 * math.pi * (hour / 24.0)
    return math.sin(angle), math.cos(angle)
