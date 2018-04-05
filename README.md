# Documentation for PyAPT


**Disclaimer**: This has been done in ~3 hours so be indulgent if you encounter
any bugs or problems with these scripts :). It's really the v0.0 of the python
version of APT. But I thought it was nice to start with something really simple
and we can then add functionnalities!

Imagine you want to do a qsub job which will launch the following commands on a
node from the all.q or the titan.q:

```
export MY_VARIABLE=42
export LD_LIBRARY_PATH=/my/lib/path/is/great:$LD_LIBRARY_PATH
cd /my/great/folder
python test.py --bar --foo 'mars'
sh /path/to/write_my_report.sh
```

Then you can simply do, from your local machine, inside a python shell:

``` python
import pyapt
pyapt.apt_run('test.py', [{'bar':None, 'foo':'mars'}], queues=['all.q', 'titan.q'],
              shell_var=[('LD_LIBRARY_PATH', '/my/lib/path/is/great/')],
	      shell_new_var=[('MY_VARIABLE', '42')],
              prepend_cmd=['cd /my/great/folder/'],
              postpend_cmd=['sh /path/to/write_my_report.sh'],
              max_parallel_jobs=1)
```

This should produce an output that looks like this:

```
You are about to launch 1 jobs on the cluster. Are you sure? [Y/n]  
Setting the max number of jobs to 1 (edit /sequoia/data1/jalayrac/tmp/90855/maxjob.inf if you wish to change that limit later)
About to launch 1 jobs on sequoia in 2s (press Ctrl+C to cancel)...
Launching!
=========================================================================================
[13-Feb-2018 16:15:05] Task 90855 : Your job 5934908 ("_0_90855") has been submitted
=========================================================================================
All your jobs have now been submitted to the cluster...
You can double checks the scripts in /sequoia/data1/jalayrac/tmp/90855/scripts/submit_*.pbs
You can double checks the logs in /sequoia/data1/jalayrac/tmp/90855/logs/report_*.txt
You can kill the jobs associated to that task by calling from the sequoia master node:
qstat -u jalayrac | grep jalayrac | grep _90855 | cut -d ' ' -f1 | xargs qdel
```


Under the hood, this will create a tmp folder (located in
/sequoia/data1/username/tmp/taskid/) containing the pbs file needed for SGE
(Sun Grid Engine), then it will launch these scripts on the cluster.

If you just want to produce the scripts but do not want to launch them from the python console,
you can do:

``` python
import pyapt
pyapt.apt_run(..., only_scripts=True)
```

[TODO]: explain other functionnalities, such as how to do grid search, grouping
jobs together...
