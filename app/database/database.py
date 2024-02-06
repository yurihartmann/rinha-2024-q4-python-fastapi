from sqlalchemy.ext.asyncio import create_async_engine, AsyncEngine, AsyncSession


class Database:
    _connection: AsyncEngine = None

    def __init__(self, db_url: str,) -> None:
        self._connection = self.__init_engine(
            db_url=db_url
        )

    @classmethod
    def __init_engine(cls, db_url: str) -> AsyncEngine:
        return create_async_engine(
            db_url,
            future=True,
            pool_pre_ping=True,
        )

    @classmethod
    def __init_async_session(cls, bind: AsyncEngine) -> AsyncSession:
        return AsyncSession(
            bind=bind,
            expire_on_commit=False,
        )

    async def factory_async_session_manager(self):
        # """
        # Get AsyncSession in async context manager
        # :param read_only:
        # :return:  AsyncSession
        # """
        async_session = self.__init_async_session(
            bind=self._connection
        )

        try:
            yield async_session
        except Exception:
            print("Error in Database.AsyncSession | Executing rollback ...")
            await async_session.rollback()
            raise
        finally:
            await async_session.close()
