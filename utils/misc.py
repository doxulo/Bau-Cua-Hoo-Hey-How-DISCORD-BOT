def get_formated_ICT_time():
    from pytz import utc, timezone
    from datetime import datetime
    return datetime.utcnow().replace(tzinfo=utc).astimezone(timezone('Asia/Ho_Chi_Minh')).strftime("%H:%M:%S %d/%m/%Y")

def author_facebook():
    return "https://www.facebook.com/doanxloc"