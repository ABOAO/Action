#!/usr/bin/env python3
"""
每天 00:00（Asia/Taipei）自動 ping 指定 API。
執行方式：python keep_alive.py
安裝：pip install requests APScheduler
"""

import time
import requests
from datetime import datetime
from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.triggers.cron import CronTrigger
from zoneinfo import ZoneInfo

URL = "https://abaoz1102-n8n-free.hf.space/healthz"

TZ = ZoneInfo("Asia/Taipei")

def ping():
    ts = int(time.time())
    url = f"{URL}?ts={ts}"
    try:
        r = requests.get(
            url,
            headers={"Cache-Control": "no-cache"},
            timeout=20,
            allow_redirects=True,
        )
        print(f"[{datetime.now(TZ).isoformat()}] ping {url} -> {r.status_code}")
        r.raise_for_status()
    except Exception as e:
        print(f"[{datetime.now(TZ).isoformat()}] ping FAILED: {e}")

if __name__ == "__main__":
    scheduler = BlockingScheduler(timezone=TZ)
    # 每天 00:00 觸發（台灣時間）
    scheduler.add_job(ping, CronTrigger(hour=0, minute=0), id="daily_ping", replace_existing=True)

    print(f"Scheduler started. TZ={TZ.key}, daily at 00:00. Target={URL}")
    # 想一啟動就先打一次，取消下一行註解
    # ping()

    scheduler.start()
