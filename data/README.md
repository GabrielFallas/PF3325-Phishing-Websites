# Data Directory

This directory contains the dataset files for the phishing detection project.

## Contents

- `Training Dataset.arff` - Original UCI Phishing Websites dataset (11,055 instances, 30 features)
- `processed/` - Preprocessed data files (generated during preprocessing, not tracked in git)

## Dataset Information

- **Source:** UCI Machine Learning Repository
- **ID:** 327
- **URL:** https://archive.ics.uci.edu/dataset/327/phishing+websites
- **Instances:** 11,055
- **Features:** 30
- **Target:** Result (-1 = phishing, 1 = legitimate)

## Loading the Dataset

### From UCI Repository (requires internet):

```python
from ucimlrepo import fetch_ucirepo

phishing_websites = fetch_ucirepo(id=327)
X = phishing_websites.data.features
y = phishing_websites.data.targets
```

### From local .arff file:

```python
from scipy.io import arff
import pandas as pd

data, meta = arff.loadarff('data/Training Dataset.arff')
df = pd.DataFrame(data)
```

## Important Notes

- The `processed/` directory is excluded from git (see `.gitignore`)
- Preprocessing scripts will automatically generate files in `processed/` when needed
- Feature values are encoded as {-1, 0, 1} (ternary encoding)
- Do NOT convert features to binary - the 0 value contains important information

