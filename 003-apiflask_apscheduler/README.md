# apiflask使用apscheduler


## 访问 apscheduler api

```
http://IP:PORT/scheduler
```

## scheduler HTTP API

```
/scheduler [GET] > returns basic information about the webapp

/scheduler/jobs [POST json job data] > adds a job to the scheduler

/scheduler/jobs/<job_id> [GET] > returns json of job details

/scheduler/jobs [GET] > returns json with details of all jobs

/scheduler/jobs/<job_id> [DELETE] > deletes job from scheduler

/scheduler/jobs/<job_id> [PATCH json job data] > updates an already existing job

/scheduler/jobs/<job_id>/pause [POST] > pauses a job, returns json of job details

/scheduler/jobs/<job_id>/resume [POST] > resumes a job, returns json of job details

/scheduler/jobs/<job_id>/run [POST] > runs a job now, returns json of job details
```

对象接口：

```
scheduler.start()

scheduler.shutdown()

scheduler.pause() > stops any job from starting. Already running jobs not affected.

scheduler.resume() > allows scheduled jobs to begin running.

scheduler.add_listener(<callback function>,<event>)

scheduler.remove_listener(<callback function>)

scheduler.add_job(<id>,<function>, **kwargs)

scheduler.remove_job(<id>, **<jobstore>)

scheduler.remove_all_jobs(**<jobstore>)

scheduler.get_job(<id>,**<jobstore>)

scheduler.modify_job(<id>,**<jobstore>, **kwargs)

scheduler.pause_job(<id>, **<jobstore>)

scheduler.resume_job(<id>, **<jobstore>)

scheduler.run_job(<id>, **<jobstore>)

scheduler.authenticate(<function>)
```
