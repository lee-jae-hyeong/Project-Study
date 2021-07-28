https://www.kaggle.com/kashnitsky/hierarchical-text-classification

Context
It's interesting to explore various approaches to hierarchical text classification.

Content
Let's start with a dataset with Amazon product reviews, classes are structured: 6 "level 1" classes, 64 "level 2" classes, and 510 "level 3" classes.
I share 3 files:

train_40k.csv - training 40k Amazon product reviews
valid_10k.csv - 10k reviews left for validation
unlabeled_150k.csv - raw 150k Amazon product reviews, these can be used for language model finetuning.
Level 1 classes are: health personal care, toys games, beauty, pet supplies, baby products, and grocery gourmet food.

Inspiration
Ideas to explore:

a "flat" approach – concatenate class names like "level1/level2/level3", then train a basic mutli-class model
simple hierarchical approach: first, level 1 model classifies reviews into 6 level 1 classes, then one of 6 level 2 models is picked up, and so on.
fancy approaches like seq2seq with reviews as input and "level1 level2 level3" strings as outputs
