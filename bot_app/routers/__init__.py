__all__ = (
    "router",
)

from aiogram import Router

from .handlers import router as handler_router

router = Router(name=__name__)

router.include_routers(
    handler_router,
)
