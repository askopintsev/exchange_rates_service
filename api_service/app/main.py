from fastapi import FastAPI


def init_app():
    app = FastAPI(
        title="Currency App",
        description="Parsing Central Bank Exchange rates",
        version="1",
    )

    from views import api
    app.include_router(
        api,
        prefix="/api/v1",
    )
    return app


app = init_app()
