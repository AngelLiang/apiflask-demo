from flask_apscheduler import APScheduler

scheduler = APScheduler()


def init_app(app):
    scheduler.init_app(app)
    scheduler.start()
    job_name_list = '|'.join([job.name for job in scheduler.get_jobs()])
    print(f'启动定时任务：{job_name_list}')


@scheduler.task('interval', id='do_job_1', seconds=30, misfire_grace_time=900)
def job1():
    print('Job 1 executed')


# cron examples
@scheduler.task('cron', id='do_job_2', minutes='*')
def job2():
    print('Job 2 executed')


@scheduler.task('cron', id='do_job_3', week='*', day_of_week='sun')
def job3():
    print('Job 3 executed')
