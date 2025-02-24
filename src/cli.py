import click

@click.command()
@click.option('--name', default='User', help='Your name.')
def greet(name):
    """Simple CLI tool to greet a user."""
    click.echo(f'Hello, {name}! Welcome to the Python CLI Tool.')

if __name__ == '__main__':
    greet()
