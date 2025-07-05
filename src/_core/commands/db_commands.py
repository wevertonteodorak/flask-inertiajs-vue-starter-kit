import click
from flask import current_app as app
from src.app.database import db

@app.cli.command('db:migrate')
def db_migrate():
    import config.models
    with app.app_context():
        db.create_all()

@app.cli.command('db:fresh')
def db_fresh():
    """Reset and Initialize the database."""
    import config.models
    db.drop_all()
    click.echo('Dropped database.')
    db.create_all()
    click.echo('Initialized database.')
