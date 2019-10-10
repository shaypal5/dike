dike ᘯ
#######

.. |PyPI-Status| |Downloads| |PyPI-Versions| |Build-Status| |Codecov| |Codefactor| |LICENCE|

Dike helps you select pre-trained word embedding for your data.

.. |dike_icon| image:: https://github.com/shaypal5/dike/blob/cc5595bbb78f784a3174a07157083f755fc93172/dike.png
   :height: 87
   :width: 40 px
   :scale: 50 %
   
.. .. image:: https://github.com/shaypal5/dike/blob/b10a19a28cb1fc41d0c596df5bcd8390e7c22ee7/dike.png

.. code-block:: python

  from dike import select_embedding
  select_embedding(df['description'])

.. contents::

.. section-numbering::


Installation
============

.. code-block:: bash

  pip install dike


Methodology
===========

``dike`` attempts to generate several metrics that might help capture the measure of representativeness/suitability of each embedding to your text data:

* **Vocabulary-based:**

  * The simple intersection between your data's vocabulary and that of the examined word embedding.
  * Vocabulary intersection weighted by word importance in your data; word importance can be given by various measures.
  * Count of missing word occurences.
  * Count of documents with at least 1/2/etc. missing words.

* **Information content:** Each document is projected into the embedding space by averaging the word vectors of the words it is composed off. Then, for each resulting projection of the entire corpus into the embedding space, the information content is estimated by presenting the number of dimension required by PCA to capture increasing thresholds of the information in the resulting space.


Use
===



Configuring dike
=================

Configure ``dike`` by populating the ``~/.config/dike/cfg.json`` file with the follosing possible configuration key-value pairs:

.. code-block:: python

  {
      "datadir": "/home/myuser/data/"  # directory where data and embedding files are downloaded to
  }



Contributing
============

Package author and current maintainer is Shay Palachy (shay.palachy@gmail.com); You are more than welcome to approach him for help. Contributions are very welcomed.

Installing for development
----------------------------

Clone:

.. code-block:: bash

  git clone git@github.com:shaypal5/dike.git


Install in development mode, including test dependencies:

.. code-block:: bash

  cd dike
  pip install -e '.[test]'


Running the tests
-----------------

To run the tests use:

.. code-block:: bash

  cd dike
  pytest


Adding documentation
--------------------

The project is documented using the `numpy docstring conventions`_, which were chosen as they are perhaps the most widely-spread conventions that are both supported by common tools such as Sphinx and result in human-readable docstrings. When documenting code you add to this project, follow `these conventions`_.

.. _`numpy docstring conventions`: https://github.com/numpy/numpy/blob/master/doc/HOWTO_DOCUMENT.rst.txt
.. _`these conventions`: https://github.com/numpy/numpy/blob/master/doc/HOWTO_DOCUMENT.rst.txt

Additionally, if you update this ``README.rst`` file,  use ``python setup.py checkdocs`` to validate it compiles.


Credits
=======

Created by `Shay Palachy <http://www.shaypalachy.com/>`_ (shay.palachy@gmail.com).

``dike`` is named after `Dike, the Greek goddess of justice <https://en.wikipedia.org/wiki/Dike_(mythology)>`_, as she is meant to help you make the right choice. The symbol ᘯ was chosen for its visual similarity to the Libra symbol, the constellation representing Dike.


.. |PyPI-Status| image:: https://img.shields.io/pypi/v/dike.svg
  :target: https://pypi.python.org/pypi/dike

.. |PyPI-Versions| image:: https://img.shields.io/pypi/pyversions/dike.svg
   :target: https://pypi.python.org/pypi/dike

.. |Build-Status| image:: https://travis-ci.org/shaypal5/dike.svg?branch=master
   :target: https://travis-ci.org/shaypal5/dike

.. |LICENCE| image:: https://img.shields.io/badge/License-MIT-yellow.svg
   :target: https://github.com/shaypal5/dike/blob/master/LICENSE

.. |Codecov| image:: https://codecov.io/github/shaypal5/dike/coverage.svg?branch=master
   :target: https://codecov.io/github/shaypal5/dike?branch=master

.. |Codacy| image:: https://api.codacy.com/project/badge/Grade/99e79faee7454a13a0e60219c32015ae
   :alt: Codacy Badge
   :target: https://app.codacy.com/app/shaypal5/dike?utm_source=github.com&utm_medium=referral&utm_content=shaypal5/dike&utm_campaign=Badge_Grade_Dashboard

.. |Requirements| image:: https://requires.io/github/shaypal5/dike/requirements.svg?branch=master
   :target: https://requires.io/github/shaypal5/dike/requirements/?branch=master
   :alt: Requirements Status
     
.. |Codefactor| image:: https://www.codefactor.io/repository/github/shaypal5/dike/badge?style=plastic
   :target: https://www.codefactor.io/repository/github/shaypal5/dike
   :alt: Codefactor code quality

.. |Downloads| image:: https://pepy.tech/badge/dike
   :target: https://pepy.tech/project/dike
   :alt: PePy stats

.. .. test pypi
