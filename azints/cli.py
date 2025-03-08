import click
from azints import __version__

@click.group()
@click.version_option(__version__, prog_name="azints")
def cli():
    """
    Azure Integrations CLI Tool

    This tool assists with managing code for Azure Integration Services.
    """
    pass

if __name__ == '__main__':
    cli()
