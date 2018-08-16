from flask import jsonify,abort

class RESP():
    def __init__(self):
        self.SUCCESS = 0
        self.SYSTEM_ERR = 11
        self.PARAMS_ERR = 21

        self.MESSAGE = {
            self.SUCCESS: "success",
            self.SYSTEM_ERR: "system error",
            self.PARAMS_ERR: "empty or wrong params",
        }

        self.REFER = {
            self.SUCCESS: "entry task success: ",
            self.SYSTEM_ERR: "system error happened",
            self.PARAMS_ERR: "empty or wrong params happened",
        }

    def response(self, code = '', data = ''):
        res = {}
        res['error_code'] = code
        res['error_message'] = self.MESSAGE[code]
        res['reference'] = self.REFER[code] + data
        return jsonify(res)

    def new_abort(self,http_status_code, *args, **kwargs):
        code = self.PARAMS_ERR if http_status_code==400 else self.SYSTEM_ERR
        abort(self.response(code=self.PARAMS_ERR))


resp = RESP()
