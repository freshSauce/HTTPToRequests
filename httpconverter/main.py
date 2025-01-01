from bs4 import BeautifulSoup, element
import autopep8
import _io
import re
from httpconverter.template import FunctionTemplate


class HTTPConverter:
    """ An HTTP converter that turns HTTP-like files into requests functions
    Parameters
    ---------
        file: str|TextIOWrapper
            Filename or object to be used, as: "file.xml" or "open('file.xml', 'r').
        source: str
            Source of the file to be used, by default burpsuite.
    """

    def __init__(self, file: str | _io.TextIOWrapper, source: str = "burpsuite") -> None:
        self._file: _io.TextIOWrapper = file
        self.source: str = source
        self.force_dicts: bool = False

        if type(file) == str:
            self._file = open(file, "r")

        self.text: BeautifulSoup = self._read_file()

    @property
    def file(self) -> str:
        return self._file.name

    @file.setter
    def file(self, new_file: str):
        try:
            self._file = open(new_file, "r")
            self.text = self._read_file()
        except IOError:
            raise Exception("File %s does not exist!" % new_file)

    @staticmethod
    def _validate_file(content: BeautifulSoup, source: str = "burpsuite") -> bool:
        if source == "burpsuite":
            items = content.find("items")
            is_burpsuite = True if items.get("burpVersion") else False
            return is_burpsuite
        else:
            raise NotImplementedError(
                "Support for other HTTP-content files is not implemented yet. Please, submit an example of your file to implement it!")

    def _read_file(self) -> BeautifulSoup :
        if self._file.name.endswith(".xml") or "." not in self._file.name:
            content = BeautifulSoup(self._file.read(), features="xml")
            if self._validate_file(content, source=self.source):
                return content
            else:
                raise NotImplementedError(
                    "Support for other HTTP-content files is not implemented yet. Please, submit an example of your file to implement it!")
        else:
            raise NotImplementedError("Support for other file types is not implemented yet.")

    @staticmethod
    def _extractor(content: BeautifulSoup, force_dicts: bool = False) -> dict:
        text = content.text
        method_endpoint_version = text.split("\n", maxsplit=1)[0]
        method, endpoint, version = method_endpoint_version.split(" ")

        headers_and_arguments = text.split("\n", maxsplit=1)[1]
        headers = headers_and_arguments.split("\n\n", maxsplit=1)[0]

        headers_as_dict = dict(
            map(lambda header: (header.split(":")[0], header.split(":", maxsplit=1)[1].lstrip()),
                filter(lambda not_empty: not_empty, headers.split("\n"))))
        if headers_as_dict.get("Cookie"):
            headers_as_dict.pop("Cookie")

        json, data, form = None, None, None
        content_type = headers_as_dict.get("Content-Type")
        if content_type:
            if "application/json" in content_type:
                json = headers_and_arguments.split("\n\n", maxsplit=1)[1]

            elif "application/x-www-form-urlencoded" in content_type:
                if not force_dicts:
                    data = headers_and_arguments.split("\n\n", maxsplit=1)[1]
                else:
                    raw_data = headers_and_arguments.split("\n\n", maxsplit=1)[1]
                    data = "{'" + raw_data.replace("=", "':'").replace("&", "', '") + "'}"

            elif "multipart/form-data" in content_type:
                args = headers_and_arguments.split("\n\n", maxsplit=1)[1]
                form = dict(
                    map(lambda item: (item.replace("\n", "").split('"')[1], item.replace("\n", "").split('"')[2]),
                        re.findall(r"name=\".*?\"\n\n.*?\n", args)))

        return dict(method=method, endpoint=endpoint, version=version, json=json, data=data, form=form,
                    headers=headers_as_dict)

    def _get_requests(self) -> element.ResultSet:
        return self.text.find_all("request")

    def extract(self, use_oop: bool = False, filename: str = "code.py", force_dicts: bool = False) -> None:
        """
        :param use_oop: Ensures the code follows a OOP syntax.
        :param filename: Name of the file where the code will be writen.
        :param force_dicts: Forces arguments to dictionary (i.e. form-data, params, etc.)
        :return:
        """
        self.force_dicts = force_dicts
        imports = "import requests\n\n"
        if use_oop:
            code = "class ClassNameHere:\n\tdef __init__(self):\n\t\tself.session = requests.Session()  # Place here your own class variables\n"
        else:
            code = ""

        code = imports + code
        all_requests = self._get_requests()
        for request in all_requests:
            content = self._extractor(request, force_dicts=force_dicts)
            template = FunctionTemplate(**content, use_oop=use_oop, force_dicts=force_dicts)
            code += template.build() + "\n\n"

        code = autopep8.fix_code(code)
        with open(filename, "w") as code_file:
            code_file.write(code)

