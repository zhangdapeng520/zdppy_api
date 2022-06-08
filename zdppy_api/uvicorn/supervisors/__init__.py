import typing

from zdppy_api.uvicorn.supervisors.basereload import BaseReload
from zdppy_api.uvicorn.supervisors.multiprocess import Multiprocess

if typing.TYPE_CHECKING:
    ChangeReload: typing.Type[BaseReload]  # pragma: no cover
else:
    try:
        from zdppy_api.uvicorn.supervisors.watchgodreload import WatchGodReload as ChangeReload
    except ImportError:  # pragma: no cover
        from zdppy_api.uvicorn.supervisors.statreload import StatReload as ChangeReload

__all__ = ["Multiprocess", "ChangeReload"]
