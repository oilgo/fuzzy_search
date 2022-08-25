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



if __name__ == '__main__':
    app()

