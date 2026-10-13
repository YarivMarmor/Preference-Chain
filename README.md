# Preference Distance — v0.2 Research Preview

Python implementation of `Module3.Macro2` from the supplied `Preference.xlsm` workbook.

## Run in Jupyter / Windows

Unzip the package. Open a Jupyter notebook in the unzipped directory and run:

```python
%run run_app.py
```

Or from the command line: `python run_app.py`.

This version requires **Python 3 with tkinter**; the GUI does not require third-party packages.

## Reference check (Cal sheet)

Input 1: `[1,1,5,1,2,3,4]`  
Input 2: `[1,2,2,2,3,4,5]`  
VBA dot product 20, squared norms 36, cosine 0.5555555556, distance 0.3125056189.

The VBA algorithm compares all item pairs, assigns +1/0/-1 for relative ranks, computes cosine similarity of the pairwise matrices and normalizes `acos(cosine)` by pi. Tied preferences are supported; however, an all-tied vector is undefined.

## Important behavior

- Both lists must contain the same number of entries, at least 2.
- Strictly integer rank labels 1..N are enforced (a deliberate validation improvement over VBA).
- Repeated ranks/ties allowed (matching original VBA).
- The comparison ignores the absolute magnitude of rankings and retains only ordering/ties.
- This preview computes a **single comparison** like the `Cal` sheet. It does not yet reproduce the workbook's large precomputed preference-distance matrices or establish their provenance.
- No EXE is built yet. Use the working Python prototype to validate the GUI first.
