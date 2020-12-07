# Content-Based Music Recommendation

> Implement a content-based muisc recommendation sytsem using using similarity learning.
> Implement other baseline content-based methods to draw comparisons from.
> Compare results over various triplet mining methods

## Data

> The chosen data set was the FMA: Free Music Archive dataset.
> Link to github repository: https://github.com/mdeff/fma

## Code

The following notebooks, scripts, and modules have been developed for the dataset.

1. [`Implementation.ipynb`]: Implementation notebook containing all the different approaches.
2. [`analysis.ipynb`]: exploration of the metadata, data, and features.
   Creates the [figures](https://github.com/mdeff/fma/tree/outputs/figures) used in the paper.
3. [`baselines.ipynb`]: baseline models for genre recognition, both from audio and features.
4. [`features.py`]: features extraction from the audio (used to create `features.csv`).
5. [`webapi.ipynb`]: query the web API of the [FMA]. Can be used to update the dataset.
6. [`creation.ipynb`]: creation of the dataset (used to create `tracks.csv` and `genres.csv`).
7. [`creation.py`]: creation of the dataset (long-running data collection and processing).
8. [`utils.py`]: helper functions and classes.

[`usage.ipynb`]:     https://nbviewer.jupyter.org/github/mdeff/fma/blob/outputs/usage.ipynb
[`analysis.ipynb`]:  https://nbviewer.jupyter.org/github/mdeff/fma/blob/outputs/analysis.ipynb
[`baselines.ipynb`]: https://nbviewer.jupyter.org/github/mdeff/fma/blob/outputs/baselines.ipynb
[`features.py`]:     features.py
[`webapi.ipynb`]:    https://nbviewer.jupyter.org/github/mdeff/fma/blob/outputs/webapi.ipynb
[`creation.ipynb`]:  https://nbviewer.jupyter.org/github/mdeff/fma/blob/outputs/creation.ipynb
[`creation.py`]:     creation.py
[`utils.py`]:        utils.py

## Usage


