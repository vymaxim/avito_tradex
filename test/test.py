import pytest

import app

def test_post_stat():
    data = {'date': '2012-12-12', 'views': 30, 'clicks': 26, 'cost': 2}
    res = app.client.post('/add_stat', json=data)
    assert res.status_code == 200

def test_get_stat():
    data = {"date_start": "2012-12-12", "date_end": "2012-12-12"}
    res = app.client.post('/get_stat', json=data)
    assert res.status_code == 200
    assert list(res.get_json()[0].keys()) == ["clicks", "cost", "cpc", "cpm", "date", "views"]

def test_get_stat_sort_clicks_asc():
    data = {"date_start": "2012-12-12", "date_end": "2012-12-12", "sort": "clicks_asc"}
    res = app.client.post('/get_stat', json=data)
    assert res.status_code == 200
    assert res.get_json()[1]["clicks"] <= res.get_json()[2]["clicks"]

def test_del_stat():
    res = app.client.delete('/del_stat')
    assert res.status_code == 200




#