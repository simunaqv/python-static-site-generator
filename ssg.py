import typer

from ssg.site import Site

def main(source="content", dest="dist"):
    config=dict()
    config["source"]= source
    config["dest"]= dest

    site = Site(**config).build()

typer.run(main)