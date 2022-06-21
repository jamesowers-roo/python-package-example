# python-package-example
An example python package

https://docs.google.com/presentation/d/1KtLruydGR-4MrZeAPHJNqpIRJS3OzlsPRNf3Nunwryc/edit#slide=id.g1244c6095bb_2_15

# 1. Quickstart

In this section we describe how install and optionally how to run the most important script/notebook.

```zsh
# 1. Clone this repo
git_home=$HOME/git  # this is the directory to clone the repo into, change this to wherever you like
mkdir -p ${git_home}
repo_name=python-package-example  # change this to the name of your repo
repo_path=${git_home}/${repo_name}
git clone git@github.com:jamesowers-roo/${repo_name}.git $repo_path

# 2. Set up a virtual env and activate it
#     - I highly recommend conda for virtual env management, it's quick to install.
conda create -n $repo_name python=3.9 --yes
conda activate $repo_name

# 3. Install the package
poetry install
```

Alternatively, you can install via github:
`pip install git+https://${GITHUB_TOKEN}@github.com/jamesowers-roo/python-package-example.git@${VERSION}`