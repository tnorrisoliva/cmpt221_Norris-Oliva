## Lab #10 - Documentation

### Pre-Lab
1. Open your `cmpt221` repository in Github and click `sync fork` > `update branch`

2. Open your `cmpt221` repository in VSCode and open your terminal.

3. Pull the changes into main using `git pull --no-edit`

4. Create a new branch for lab 9 using `git checkout -b lab-10`

5. Create and activate your virtual environment

6. Install requirements.txt with `pip install -r requirements.txt`


### Lab 
#### 1. Install Sphinx
Install Sphinx using Pip.  
**Note:** You'll want to include this in your requirements.txt file
```bash
# -U ensures we get the most up to date version
pip install -U sphinx
```

#### 2. Set up the Sphinx source directory

`cd` into the `labs/lab-10/docs` directory

```bash
sphinx-quickstart
# or
python3 -m sphinx.cmd.quickstart
# or
python -m sphinx.cmd.quickstart
```

Run through the configuration script:
```
> Separate the source and build directories (y/n) [n]: n
> Project name: CMPT221
> Author name(s): Your name
> Project release []: 0.0.1
> Project language [en]: en
```

#### 3. Define your documentation structure
The `sphinx-quickstart` command created a source directory with `conf.py` and a root document, `index.rst`.   

The main function of `index.rst` is to serve as a welcome page and to contain the root of the "table of contents tree" (a.k.a toctree). The toctree is what connects all of your documentation pages to the welcome page (index.rst).

toctree is a reStructuredText directive. A directive can have arguments, options, and content.   
- Arguments are given directly after the double colon following the directive's name. Each directive decides whether it can have arguments, and how many.  
- Options are given after the arguments, in form of a "field list". `maxdepth` is an option for the toctree directive.  
- Content follows the options or arguments after a blank like. Each directive decides whether to allow content, and what to fo with it. _The first line of content must be intented to the same level as the options_

Add the following pages to the content in your toctree in `index.rst`:
- introduction.rst
- development.rst
- resources.rst
- troubleshooting.rst

#### 4. Add content to the .rst files
Create documentation for the CMPT221 lab repository by following the prompts in the .rst templates provided.

#### 5. Deploy your documentation
To deploy your documentation, issue:
```bash
make html
# for windows users without make installed:
make.bat html
```

then, create a gh-pages branch
```bash
git checkout -b gh-pages
```

Drag all of the HTML from docs/_build/html into root and delete everything else (yes, really)

### Submission
Once you have completed this lab, push your work to Github, then open a pull request, assign me as a reviewer, copy the pull request URL, and paste it in Brightspace. Don't forget to deactivate your virtual environment!

```bash
git add .
git commit -m "completed lab 9"
git push --set-upstream origin lab-9
# or
git push
```

