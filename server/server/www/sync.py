from server import app
from server.www.base import mobile_request, must_login
import server.logic.sync as logic_sync


@app.route("/sync", methods=['PUT'])
@mobile_request
@must_login
def sync_data(user_id, sync_token=None, sync_items=[], **kwargs):
    return logic_sync.sync_data(user_id, sync_token, sync_items)