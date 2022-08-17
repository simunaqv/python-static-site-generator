import typer
import sys
from docutils.core import publish_parts
from markdown import markdown
from ssg.content import Content

from ssg.site import Site

def main(source="content", dest="dist"):
    config={"source": source, "dest": dest}

    site = Site(**config).build()

typer.run(main)