# Documentation for PyAPT


**Disclaimer**: This has been done in ~3 hours so be indulgent if you encounter any bugs or problems with these scripts :). It's really the v0.0 of the python version of APT. But I thought it was nice to start with something really simple and we can then add functionnalities!

Imagine you want to do a qsub job which will launch the following commands on a node from the all.q or the titan.q:

```
export LD_LIBRARY_PATH=/my/lib/path/is/great:$LD_LIBRARY_PATH
cd /my/great/folder
python test.py --foo='mars'
sh /path/to/write_my_report.sh
```

Then you can simply do, from your local machine, inside a python shell:

```
   import pyapt
   pyapt.apt_run('test.py', [{'foo':'mars'}], combine_args=False, queues=['all.q', 'titan.q'],shell_var=[('LD_LIBRARY_PATH', '/my/lib/path/is/great/')], prepend_cmd=['cd /my/great/folder/'], postpend_cmd=['sh /path/to/write_my_report.sh'], max_parrallel_jobs=1)
```

Under the hood, this will create a tmp folder (located in /sequoia/data1/username/tmp/taskid/) containing the pbs file needed for SGE (Sun Grid Engine), then it will launch these scripts on the cluster.

[TODO]: explain other functionnalities, such as grid search, grouping jobs together...
