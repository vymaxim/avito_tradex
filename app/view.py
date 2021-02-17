from flask import request, jsonify
from werkzeug.exceptions import abort
from app import app
from app.exeption import *


def page_not_found(err_description):
    return jsonify(error=str(err_description)), 404


def incorrect_input(err_description):
    return jsonify(error=str(err_description)), 400


app.register_error_handler(404, page_not_found)
app.register_error_handler(400, incorrect_input)


@app.route('/get_stat', methods=['POST'])
def get_statistics():
    try:
        request_body = dict(request.json)
        date_start = request_body['date_start']
        date_end = request_body['date_end']
        if 'sort' in request_body:
            sort = request_body['sort']
        else:
            sort = 'None'
        from app import interaction
        return jsonify(interaction.get_statistics(date_start=date_start, date_end=date_end, sort=sort)[0])
    except IncorrectInputException:
        abort(400, description=f'incorrect sort value')


@app.route('/add_stat', methods=['POST'])
def add_statistics():
    request_body = dict(request.json)
    if 'date' in request_body:
        date = request_body['date']
    else:
        date = None
    if 'views' in request_body:
        views = float(request_body['views'])
    else:
        views = None
    if 'clicks' in request_body:
        clicks = float(request_body['clicks'])
    else:
        clicks = None
    if 'cost' in request_body:
        cost = float(request_body['cost'])
    else:
        cost = None
    from app import interaction
    return interaction.save_statistics(
        date=date,
        views=views,
        clicks=clicks,
        cost=cost
    )


@app.route('/del_stat', methods=['DELETE'])
def del_statistics():
    try:
        from app import interaction
        return interaction.clear_statistics()
    except BaseClearException:
        abort(404, description=f'Base already clear')