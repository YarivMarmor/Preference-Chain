# Preference Chain — Preference Ranking Distance Tool

**A standalone Windows application for measuring distances between preference rankings, including tied preferences.**

Preference Chain is a Python-based implementation of a preference-distance calculation originally developed in Excel/VBA.

The software supports comparing two preference rankings using a cosine-based similarity measure and a normalized angular distance. It is associated with the research methodology presented by Vanacore, Marmor, and Bashkansky (2019).

**Current version:** v0.2.0 — Research Preview

## Download for Windows

**[Download PreferenceChain.exe — Windows application](https://github.com/YarivMarmor/Preference-Chain/releases/download/v0.2.0-preview/PreferenceChain.exe)**

Preference Chain runs as a standalone Windows application. No installation of Python, Jupyter, or Microsoft Excel is required.

To get started:

1. Download `PreferenceChain.exe`.
2. Save the executable to your computer.
3. Double-click the file to launch the application.
4. Enter two preference rankings or load them from TXT/CSV files.
5. Click **Calculate** to obtain the similarity and distance.
6. Optionally export the results to CSV.

### Windows security notice

The executable is not digitally signed. Windows may display an *Unknown publisher* or *Windows protected your PC* warning.

If you have verified that the file originates from this official GitHub Release and your organization's security policy permits it, you may select **More info → Run anyway**, where available.

Do not disable Windows security protections.

## Main features

- Comparison of two preference rankings.
- Support for tied preferences (weak orders).
- Calculation of cosine similarity using the original VBA-compatible pairwise ordering representation.
- Calculation of normalized angular distance.
- Manual entry of preference rankings.
- Loading rankings from TXT or CSV files.
- Export of calculation results to CSV.
- Standalone Windows executable.
- Publicly available Python source code.

## How the method works

Preference rankings describe the relative priority assigned to a set of alternatives or criteria.

The software evaluates two preference chains by converting their pairwise ordering relationships into the representation used in the original VBA implementation.

The resulting cosine similarity is converted to a normalized angular distance:

\[
d(P_1,P_2)=\frac{\arccos(\operatorname{Cosine}(P_1,P_2))}{\pi}
\]

The normalized angular distance is between 0 and 1.

Smaller distances indicate greater similarity between the preference chains. A distance of zero indicates identical pairwise ordering representations.

The implementation supports tied ranks, where two or more alternatives receive the same priority.

## Input data

Rankings can be entered directly into the application, with one rank per line or using comma- or space-separated values.

Each position corresponds to the same alternative in both rankings.

For example:

**Preference 1**

```text
1
1
5
1
2
3
4
```

**Preference 2**

```text
1
2
2
2
3
4
5
```

The example contains tied preferences and is included in the application.

Both rankings must refer to the same set of alternatives, in the same order.

## Reference calculation

The example from the original Excel/VBA workbook was reproduced in Python.

| Metric | Reference result |
|---|---:|
| Cosine similarity | 0.555555556 |
| Normalized angular distance | 0.312505619 |
| Numerator | 20 |
| Norm 1 | 36 |
| Norm 2 | 36 |

The displayed results agree with the original Excel reference example to the reported precision.

This confirms reproduction of the reference calculation, but does not constitute complete validation of all workbook functionality.

## Scientific publication

The associated research methodology is presented in:

**Vanacore, A., Marmor, Y. N., & Bashkansky, E. (2019).** Some metrological aspects of preferences expressed by prioritization of alternatives. *Measurement, 135*, 520–526.

**DOI:** https://doi.org/10.1016/j.measurement.2018.11.012

The publication discusses metrological aspects of preference assessment, including similarity between preference chains and considerations of repeatability and reproducibility.

Researchers using the methodology are encouraged to cite the original scientific article.

The repository also supports software citation through the `CITATION.cff` file once added.

## Run from Python

Researchers and developers can run the application directly from the source code.

Python 3 with Tkinter support is required.

From the repository directory:

```bash
python run_app.py
```

The current graphical application does not require additional third-party Python packages.

## Testing and validation

The Python implementation was checked against the reference example from the Excel/VBA workbook.

Six automated tests passed, and the standalone Windows executable was successfully launched and tested.

The CSV export was also checked using Microsoft Excel.

To run the automated tests:

```bash
python -m pytest tests -q
```

The repository includes example preference-distance matrices derived from the original workbook for further validation.

## Research Preview — scope and limitations

**Version 0.2.0 is a research preview.**

The current release implements the pairwise preference-distance calculation from the original VBA tool.

The following work remains:

- Complete numerical validation against the original workbook's three preference-distance matrices.
- Implementation of full pairwise distance-matrix generation for multiple preference chains.
- Review of additional analytical functionality associated with the original research methodology.
- Further testing of input validation, edge cases, and numerical reproducibility.

The current software should not be regarded as a complete implementation of every analysis presented in the scientific publication.

## Building the Windows executable

The Windows application is built using PyInstaller and GitHub Actions.

The automated workflow runs the tests, builds a standalone Windows executable, and attaches `PreferenceChain.exe` to a published GitHub Release.

**Releases:** https://github.com/YarivMarmor/Preference-Chain/releases

## Feedback and contributions

Bug reports, suggestions, and research feedback are welcome.

**GitHub Issues:** https://github.com/YarivMarmor/Preference-Chain/issues

Feedback concerning numerical agreement with Excel/VBA, tied rankings, and distance calculations is especially valuable.

## Author

**Dr. Yariv N. Marmor**

Department of Industrial Engineering and Management  
Braude College of Engineering, Israel

**ORCID:** https://orcid.org/0000-0001-9200-5041

**GitHub:** https://github.com/YarivMarmor

## License

This software is distributed under the MIT License. See the [LICENSE](LICENSE) file for details.
