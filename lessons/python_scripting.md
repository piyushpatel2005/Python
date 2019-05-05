# Python Scripting

Python is one of the powerful programming languages built into every UNIX based systems.
It can be used for easier scripting than Bash.

[Interacting with files](../examples/files)

[Interacting with environment variables](../examples/env)

[Interact with User input](../examples/age)

[Interact with arguments](../examples/reverse-file)

[Error handling](../examples/error)

[working on Subprocess](../examples/cmd)

[Exit status](../examples/pexit)

[List comprehension](../examples/contains)

[Generate json](../examples/receipts/gen_receipts.py)

[Process files shutil](../examples/receipts/process_receipts.py)

We can install various other packages using `pip`.

To install `pip` on CentOS.

```shell
sudo um install epel-release
sudo yum update
sudo yum upgrade python-setuptools
sudo yum install -y python-pip python-wheel
pip -V
sudo pip install --upgrade pip
pip -V
pip list
```

`sudo pip install boto3` to AWS client.
or `pip install --user boto3` to install on user level.

`pip list --user --format=columns`

`pip freeze --user` would display version of each packages.

```shell
pip freeze --user | grep boto3 > requirements.txt
pip install --user -r requirements.txt # to install packages
pip uninstall boto3 # uninstall package
pip freeze --user > requirements.txt
pip uninstall -r requirements.txt # uninstall all packages
```

**virtualenv** is a sand-boxed python environment.

```shell
pip install --user virtualenv
which virtualenv
mkdir venvs
virtualenv venvs/experiment
source venvs/experiment/bin/active
pip list
pip install flask
pip list
deactivate
pip list | grep Flask
