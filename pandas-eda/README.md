# Ratings vs. Bestseller Status

Exploratory data analysis comparing users feedback (Goodreads ratings) against commercial popularity (NYT bestseller list appearances) for canonically "top" novels.

  **Research question:** Is there a correlation between a novel's user rating 
  on Goodreads and its commercial popularity (measured as weeks on the NYT
  bestseller list)?   

 **Datasets:**                                                               
  - **Top 500 Novels** — from Responsible Datasets in Context](https://www.responsible-datasets-in-context.com/posts/top-500-novels/) (Melanie
  Walsh). Contains 500 canonically "top" novels with Goodreads metadata.      
  - **NYT Bestsellers** — from [Post45](https://github.com/ecds/post45-datasets). Every NYT bestseller list entry from
  1931 onward (60,386 weekly rankings). 

  **Approach:**
  1. Work with NYT dataset on composing on how often each book was on the list and whats the highest rank it achieved?
  2. Merge that aggregated table with the Top 500 Novels dataset on title + author.   
  3. Caclulate Pearsons correlation on weeks on the list with ranking and saleability. 
  4. Create 2 scatter graphs with Altair

## Files

- `RatingsVsBestsellerStatus.ipynb` — the analysis notebook
- `top-500-novels.tsv` — local copy of the top-500 dataset
- `nyt_full.tsv` — local copy of the NYT dataset

## How to run

1. Make sure you have Python 3 with `pandas` and `altair` installed:
   ```bash
   pip install pandas altair
   ```
2. Open `RatingsVsBestsellerStatus.ipynb` in Jupyter or VS Code.
3. Click **Restart** then **Run All**.

The notebook reads the `.tsv` files from the same folder, so no internet connection is required.

## Notebook structure

1. **Load Data** — read both TSV files into pandas
2. **Aggregate NYT** — collapse weekly rankings into one row per book with `weeks_on_list` and `best_rank`
3. **Merge** — join with the top-500 novels on title + author
4. **Correlation** — compute Pearson correlation coefficient
5. **Visualization** — Altair scatter plot with regression line
6. **Findings** — interpretation of results and limitations
