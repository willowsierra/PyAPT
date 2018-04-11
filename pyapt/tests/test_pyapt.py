import os
import re
import glob

import pyapt


def check_pbs_script(python_script, filename, arg_dict):
    with open(filename) as script_file:
        script_content = script_file.read()
    assert 'python {}'.format(python_script) in script_content
    str_arguments = ['--{} {!r}'.format(arg_name, str(arg_value))
                     for arg_name, arg_value in arg_dict.items()]
    for str_arg in str_arguments:
        assert str_arg in script_content


def test_apt_run(tmpdir, capsys):
    root_folder = tmpdir.strpath
    args = [{'kernel': 'linear', 'C': 1},
            {'kernel': 'rbm', 'C': 1e-3, 'gamma': 1}]
    python_script = 'test.py'
    task_id = pyapt.apt_run(python_script,
                            args,
                            only_scripts=True,
                            tmp_dir=root_folder)
    task_folder = os.path.join(root_folder, task_id)
    stdout, stderr = capsys.readouterr()
    assert stderr == ''
    scripts_glob = re.search(r'.+scripts have been created[^/]+(/[\w\-/.*]+)',
                             stdout).group(1)
    assert scripts_glob.startswith(task_folder)
    scripts = sorted(glob.glob(scripts_glob))
    assert len(scripts) == len(args)

    launcher_script = re.search(r'.+launch[^/]+(/[\w\-/.]+)',
                                stdout).group(1)
    assert launcher_script.startswith(task_folder)
    assert os.path.isfile(launcher_script)

    for script, arg_dict in zip(scripts, args):
        check_pbs_script(python_script, script, arg_dict)
