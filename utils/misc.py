def get_formated_ICT_time():
    from pytz import utc, timezone
    from datetime import datetime
    return datetime.utcnow().replace(tzinfo=utc).astimezone(timezone('Asia/Ho_Chi_Minh')).strftime("%H:%M:%S %d/%m/%Y")

def get_formated_uptime(starttime):
    import datetime
    import time
    uptime = str(datetime.timedelta(seconds=int(round(time.time()-starttime)))).split(':')
    return f"{uptime[0]}h:{uptime[1]}m:{uptime[2]}s"

def get_raw_current_time():
    import time 
    return time.time()

def author_facebook():
    return "https://www.facebook.com/doanxloc"

def current_time():
    from datetime import datetime 
    return datetime.now()