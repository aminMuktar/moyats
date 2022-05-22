import time
from .base import BaseTask
from decimal import Decimal
from moyats.celery import app
from celery_progress.backend import ProgressRecorder

# Boilerplate code for running background processes with celery beat
#
# CAll process with delay instance
# response = init_bg_process.delay(*args)
# task_id = response.task_id
# 

#
#
#


class RunBackgroundTask(BaseTask):
    name = "RunBackgroundTask"

    def __init__(self) -> None:
        self.ttask_id = None

    def progress(self, duration, time_):
        current = round(time_ / duration * 100)
        total = 100
        percent = 0
        if total > 0:
            percent = (Decimal(current) / Decimal(total)) * Decimal(100)
            percent = float(round(percent, 2))

        self.update_state(
            task_id=self.ttask_id,
            state='PROGRESS',
            meta={
                'current': current,
                'total': total,
                'percent': percent,
            }
        )

    def run(self, *args, **kwargs):
        progress_recorder = ProgressRecorder(self)
        for x in range(0, 100):
            time.sleep(1)
            progress_recorder.set_progress(
                x, total=100, description=f"Running {x}")

        return {
            "detail": "success"
        }


@app.task(bind=True, base=RunBackgroundTask)
def init_bg_process(self, *args, **kwargs):
    return super(type(self), self).run(*args, **kwargs)
