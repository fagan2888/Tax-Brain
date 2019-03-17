# Tax-Brain

Tax-Brain is a Python package that wraps multiple economic models in one easy
to use interface.

## Overview

Tax-Brain makes it easy for users to simulate the US tax system by providing a
single interface for multiple tax models. Currently, Tax-Brain interfaces with
[Tax-Calculator](https://github.com/PSLmodels/Tax-Calculator) and
[Behavior-Response](https://github.com/PSLmodels/Behavioral-Responses).
Additional models will be added in the near future to expand Tax-Brain's
capabilities to include modeling business taxation and running dynamic
general equilibrium simulations.

To learn more about how Tax-Brain works, see [this](https://github.com/PSLmodels/Tax-Brain/blob/master/DOC.md)
document.

## Disclaimer

Tax-brain and it's underlying models are constantly being improved upon. For
that reason, the results output by Tax-Brain may differ over time. It is
strongly suggested that the user make note of which version of Tax-Brain,
they are using when reporting their results.

## Installing Tax-Brain

You can install the latest official release from Conda using this command:
`conda install -c pslmodels taxbrain`.

Similarly, you can update to the latest release of Tax-Brain using
`conda update -c pslmodels taxbrain`.

Tax-Brain is currently not available on PyPI.

## Using Tax-Brain

View the sample code in [example.py](example.py) to see how to run Tax-Brain

## Citing Tax-Brain

Please cite the source of your analysis as "Tax-Brain release #.#.#, author's
calculations." If you would like to link to Tax-Brain, please use
`https://github.com/PSLmodels/Tax-Brain`. It is also strongly suggested that
you describe your input data and note the versions of the underlying models.

## Additional Information

* [Project Road Map](ROADMAP.md)
* [Contributors](https://github.com/PSLmodels/Tax-Brain/graphs/contributors)
* [Release History](https://github.com/PSLmodels/Tax-Brain/blob/master/RELEASES.md)