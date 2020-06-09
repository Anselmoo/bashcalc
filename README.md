# bashcalc
## Instant calculating from the terminal into the terminal
---

`bashcalc` is an instant command-line tool for calculating directly mathematical expression into the terminal. 

It is designed for working on cluster-server, where numbers or expressions have to be calculated without starting a new application or blogging any terminal windows. Therefore it will just show the result and immediately close. For this purpose,  it is a pure `python` based and does not require any additional packages.

The idea is 

```unix
╰─ bashcalc 1230/2
>>> 615
```

## Installation
---
```pip install bashcalc```

or

```pip install https://github.com/Anselmoo/bashcalc.git```

or 

```bash
python setup.py install
```
## Author
---

 * [Anselm Hahn](https://github.com/Anselmoo)

## Contributions
---

I'm happy to accept how to improve batchplot; please forward your [issues](https://github.com/Anselmoo/bashcalc/issues) or [pull requests](https://github.com/Anselmoo/bashcalc/pulls).

Keep in mind that [pull requests](https://github.com/Anselmoo/bashcalc/pulls) have to pass TravisCI in combination with [flake8](https://github.com/PyCQA/flake8), [black](https://github.com/psf/black), and [pydocstyle](https://github.com/PyCQA/pydocstyle).

## License
---

The source code of `bashplot` is licensed under the [MIT license](https://github.com/Anselmoo/bashcalc/blob/master/LICENSE).
