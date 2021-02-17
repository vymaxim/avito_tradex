from app import session, Statistics
from app.exeption import *


def get_statistics(date_start, date_end, sort):
    sort_list = {
        "None": Statistics.date.asc(),
        "date_asc": Statistics.date.asc(),
        "date_desc": Statistics.date.desc(),
        "views_asc": Statistics.views.asc(),
        "views_desc": Statistics.views.desc(),
        "clicks_asc": Statistics.clicks.asc(),
        "clicks_desc": Statistics.clicks.desc(),
        "cost_asc": Statistics.cost.asc(),
        "cost_desc": Statistics.cost.desc(),
        "cpc_asc": Statistics.cpc.asc(),
        "cpc_desc": Statistics.cpc.desc(),
        "cpm_asc": Statistics.cpm.asc(),
        "cpm_desc": Statistics.cpm.desc()
    }
    if sort in sort_list:
        statistics = session.query(Statistics).filter(Statistics.date >= date_start, Statistics.date <= date_end).order_by(sort_list[sort]).all()
        if statistics:
            statistics_list = []
            for stat in statistics:
                stat = {'date': stat.date, 'views': stat.views, 'clicks': stat.clicks, 'cost': stat.cost, 'cpc': stat.cpc,
                        'cpm': stat.cpm}
                statistics_list.append(stat)
            return statistics_list, 200
    else:
        raise IncorrectInputException

def save_statistics(date, views=None, clicks=None, cost=None):
    statistics = Statistics(
        date=date,
        views=views,
        clicks=clicks,
        cost=round(cost, 2),
        cpc=round(cost / clicks, 2),
        cpm=round(cost / views * 1000)
    )
    session.add(statistics)
    session.commit()
    return f'Success', 200


def clear_statistics():
    statistics = session.query(Statistics).all()
    if statistics:
        for i in statistics:
            session.delete(i)
            session.commit()
        return f'Statistics clear', 200
    else:
        raise BaseClearException
