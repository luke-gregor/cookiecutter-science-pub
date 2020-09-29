---
bibliography: [../referencing/library.bib]
---

# The living docs

Focus on making your project easy to navigate and view by yourself and others. The living docs will become your reference as the project progresses and grows. This also shifts the focus to writing rather than coding (which is something that I struggle with). 

## `tl;dr`

1. navigate to the `docs` folder in the terminal
2. run the command: `mkdocs serve` and go to [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
3. changes in the `writing/markdown/` folder will automatically be updated to the living documentation
4. cite your references in `writing/referencing/library.bib` using @referenceKey

## Setup and installation
You will need to run the following line of code to install dependencies:
`pip install mkdocs mkdocs-material mkdocs-bibtex`

## How it works
In the base directory of the project, there is the `docs` directory that contains a file called `mkdocs.yml`. This is configuration file that tells the `mkdocs` package how to compile your living docs (a.k.a. a website!). Running the `mkdocs serve` command from the `docs` directory in the terminal will run a local server that you can see changes to your project website live. 

The `mkdocs.yml` file is set up so that it looks for files in the `writing/markdown` folder. Any files will automatically be added to the website. If you have folders in the directory with `.md` files, your web page will be hierarchical with the folder name representing the links in the header and files are the links in the left navigation bar. 

Note that changing the contents of this `README.md` file will change the landing page. You can also create a symbolic link to the project readme - this might be more suitable once you have read these docs. Or you could move it to a new folder so you can read it later. 

## References and citations
MkDocs also supports bibtex citations using the [mkdocs-bibtex](https://pypi.org/project/mkdocs-bibtex/) extension. This means you can export your library from Mendeley/Zotero as a `.bib` file. The `mkdocs.yml` file is configured to look for your `.bib` file in `writing/referencing/library.bib`. There is also an option to set the style of your citations using a `.csl` file (also used in LaTeX) but I'm not sure this is working at the moment. 

I also recommend that you use an extension in your text editor or whatever you decide to use that will create prompts for the references in your `library.bib` file. Here's a link to the VS Code extension for [Pandoc Citer](https://marketplace.visualstudio.com/items?itemName=notZaki.pandocciter).


`[@Key]` can be used to create citations as footnotes[@Example].

\bibliography
