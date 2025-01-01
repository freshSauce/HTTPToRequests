[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![GNU GPLv3 License][license-shield]][license-url]
[![Telegram][telegram-shield]][telegram-url]


# HTTPToRequests

Tired of translating HTTP Messages to Python requests by hand or doing a curl->requests translation everytime? Say no more! Here is HTTPToRequests, a tool that let you translate HTTP messages to python code ready to use!
## Features

- CLI/Module use
- Support for burpsuite
- Easy to use
- Support for OOP styled code or only functions.


## Usage/Examples

Usage within code:
```python
from httpconverter import HTTPConverter 

file = "./examples/example.xml"

converter = HTTPConverter(file)
converter.extract() # Optional flags:
                    # use_oop - Write OOP styled code or just the functions. False by default
                    # force_dicts - Forces arguments to dictionary (i.e. form-data, params, etc.). False by default
```

CLI usage:
```bash
$ python -m httpconverter.cli --file ./examples/example.xml --output example.py
$ File converted and saved to example.py

```



## Installation

You can install the script to access it anywhere.

```bash
  python setup.py install
  httpconverter --file FILE.xml --output OUTPUT.py
```
    
## Running Tests

To run tests, run the following command

```bash
  pytest .\tests\
```


## License

Distributed under the GNU GPLv3 License. See `LICENSE` for more information.




## Contributing

Want to contribute to the project? Great! Please follow the next steps in order to submit any feature or bug-fix :) You can also send me your ideas to my [Telegram](https://t.me/freshSauce), any submit is **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

[contributors-shield]: https://img.shields.io/github/contributors/freshSauce/HTTPToRequests.svg?style=for-the-badge
[contributors-url]: https://github.com/freshSauce/HTTPToRequests/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/freshSauce/HTTPToRequests.svg?style=for-the-badge
[forks-url]: https://github.com/freshSauce/HTTPToRequests/network/members
[stars-shield]: https://img.shields.io/github/stars/freshSauce/HTTPToRequests.svg?style=for-the-badge
[stars-url]: https://github.com/freshSauce/HTTPToRequests/stargazers
[issues-shield]: https://img.shields.io/github/issues/freshSauce/HTTPToRequests.svg?style=for-the-badge
[issues-url]: https://github.com/freshSauce/HTTPToRequests/issues
[license-shield]: https://img.shields.io/github/license/freshSauce/HTTPToRequests.svg?style=for-the-badge&cacheSeconds=3600
[license-url]: https://github.com/freshSauce/HTTPToRequests/blob/main/LICENSE
[telegram-shield]: https://img.shields.io/badge/-@freshSauce-black?style=for-the-badge&logo=telegram&colorB=0af
[telegram-url]: https://t.me/freshSauce
