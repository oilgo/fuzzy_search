import os, typer, uvicorn
from typing import Optional
from core.config import HOST, PORT


app = typer.Typer()


@app.command()
def version():
    """ Test command to get python version
    """

    os.system('python --version')



@app.command()
def runserver(
    reload: Optional[bool] = True
):
    """ Command to run uvicorn server
    """

    typer.secho(
        message = f'\nRun server...\n',
        fg = typer.colors.BRIGHT_GREEN)

    uvicorn.run(
        app = 'main:app',
        host = HOST,
        port = PORT,
        reload = reload)


@app.command()
def makemigrations(name: Optional[str] = None):
    ''' Make migrations'''
    typer.secho(
        message= f"\nStart creating alembic migration file...\n",
        fg = typer.colors.BRIGHT_GREEN
    )

    if name:
        os.system(f"alembic revision --autogenerate -m { name }")
    else:
        os.system(f"alembic revision --autogenerate")


@app.command()
def migrate():
    ''' Apply migrations to the database.
        >>> python manage.py migrate
    '''
    typer.secho(
        message= f"\nStart migrating...\n",
        fg = typer.colors.BRIGHT_GREEN
    )

    os.system(f"alembic upgrade head")


if __name__ == '__main__':
    app()

