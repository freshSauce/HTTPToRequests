class FunctionTemplate:
    def __init__(self, method, endpoint, version, headers, form=None, params=None, json=None, data=None, use_oop=False, force_dicts=False):
        self.method: str = method
        self.endpoint: str = endpoint
        self.version: str = version
        self.headers: dict = headers
        self.data: dict|str = data
        self.form: dict = form
        self.params: dict = params
        self.json: dict = json
        self.use_oop: bool = use_oop
        self.force_dicts: bool = force_dicts

    def build(self):

        function = "def {function_name}(" + ("self" if self.use_oop else "session") + "):\n" \
                   + "\theaders = {headers}\n" \
                   + ("\tjson = {json}\n" if self.json else "") \
                   + ("\tdata = '{data}'\n" if self.data and not self.force_dicts else "\tdata = {data}\n" if self.data and self.force_dicts else "") \
                   + ("\tparams = {params}\n" if self.params else "") \
                   + ("\tform = {form}\n\n" if self.form else "\n")

        if self.use_oop:
            request_body = "\tresponse = self.session.{method}('{url}', headers=headers, " \
                           + ("json=json, " if self.json else "") \
                           + ("data=data, " if self.data else "") \
                           + ("params=params, " if self.params else "") \
                           + ("files=form)" if self.form else ")")
        else:
            request_body = "\tresponse = session.{method}('{url}', headers=headers, " \
                           + ("json=json, " if self.json else "") \
                           + ("data=data, " if self.data else "") \
                           + ("params=params, " if self.params else "") \
                           + ("files=form)" if self.form else ")")

        if self.use_oop:
            function = "\t" + function.replace("\t", "\t\t")
            request_body = request_body.replace("\t", "\t\t")

        template = function + request_body
        endpoint_parts = self.endpoint.split("?")[0].strip("/").split("/")
        function_name = "_".join([self.method.lower()] + endpoint_parts)

        return template.format(
            function_name=function_name.replace(".", "_").replace("-", "_"),
            headers=self.headers.__repr__(),
            json=self.json if self.json else {},
            data=self.data if self.data else {},
            params=self.params if self.params else {},
            method=self.method.lower(),
            form=self.form if self.form else {},
            url=f"https://{self.headers['Host']}{self.endpoint}"
        )