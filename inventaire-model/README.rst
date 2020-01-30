inventaire-model
--------


tests
    python3 setup.py test

sdist
    python3 setup.py sdist
upload
    twine upload -u admin -r pypi --config-file ~/.pip/.pypirc dist/*

install
    pip install inventaire-model

To use (with caution), simply do::

    >>> from models import medias
    >>> m = medias.Media(1, "Python", "SG")
    >>> print(m)