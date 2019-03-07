import abc
from pathlib import Path

import pandas as pd


SENSITIVE_ATTRIBUTES = ['race', 'gender']


class Dataset(abc.ABC):
    @abc.abstractmethod
    def __init__(self, path, sensitive_attributes):

        p = Path(path)

        self.df = pd.read_csv(path)
        self._preprocess()

        self._name = self.__doc__.splitlines()[0]

        self.sensitive_attributes = sensitive_attributes

        self._validate()

    def __str__(self):
        return ('<{}: {} rows, {} columns'
                ' in which {} are sensitive attributes>'
                .format(self._name,
                        len(self.df),
                        len(self.df.columns),
                        self.sensitive_attributes))

    @abc.abstractmethod
    def _preprocess(self):
        pass

    @abc.abstractmethod
    def _validate(self):
        assert all(attr in SENSITIVE_ATTRIBUTES
                   for attr in self.sensitive_attributes),\
         ('the sensitive attributes {} can be only from {}.'  # noqa
          .format(self.sensitive_attributes, SENSITIVE_ATTRIBUTES))