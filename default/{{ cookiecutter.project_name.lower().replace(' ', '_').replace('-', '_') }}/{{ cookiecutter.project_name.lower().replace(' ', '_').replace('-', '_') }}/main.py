import typer

app = typer.Typer()


@app.command()
def run():
    """run @app.command annoted functions using poetry run func."""
    app()


def main():
    pass

if __name__ == "__main__":
    main()
