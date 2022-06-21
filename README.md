# python-package-example
An example python package

https://docs.google.com/presentation/d/1KtLruydGR-4MrZeAPHJNqpIRJS3OzlsPRNf3Nunwryc/edit#slide=id.g1244c6095bb_2_15

# 1. Quickstart

In this section we describe how install and optionally how to run the most important script/notebook.

```zsh
# 1. Clone this repo
git_home=$HOME/git  # this is the directory to clone the repo into, change this to wherever you like
mkdir -p ${git_home}
repo_name=roo-python-package-example  # change this to the name of your repo
repo_path=${git_home}/${repo_name}
git clone git@github.com:jamesowers-roo/${repo_name}.git $repo_path

# 2. Set up a virtual env and activate it
#     - I highly recommend conda for virtual env management, it's quick to install.
conda create -n $repo_name python=3.10 --yes
conda activate $repo_name

# 3. Install the package and scripts, along with:
#     - the `-e` flag, 'editable' mode: changes to local files will affect package (this
#     means that you will not need to reinstall )
#     - all package dependencies (listed in setup.cfg under install_requires)
#     - extra `[dev]` packages (listed in setup.cfg under [options.extras_require])
#     functionality without the need to reinstall the package
pip install -e "${repo_path}[dev]"

# 4. (Optional) Run installed scripts - these were installed by the pip install above
example_bash_script
example_python_script
example_python_executable --help
example_python_executable --sequence-length 20
```