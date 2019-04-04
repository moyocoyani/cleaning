def approx_years(startdate,enddate,_format='%Y-%m-%d'):
    from datetime import datetime, timedelta
    if _format == 'None':
        return np.floor((enddate- startdate)/timedelta(days=365.2425))
    else:
        return np.floor((datetime.strptime(enddate,_format) - startdate)/timedelta(days=365.2425))
