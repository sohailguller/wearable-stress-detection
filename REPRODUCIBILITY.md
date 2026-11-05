# Data access and verification

Obtain the source data from [Zenodo record 6640290](https://zenodo.org/records/6640290). Cite the dataset separately from this analysis. Keep downloads and participant-level intermediates outside version control. Record the exact files, versions and checksums used when verifying the analysis.

To reproduce the study, obtain the original notebooks/scripts and their inputs. Document the execution order, environment versions, event matching and exclusion rules, baseline construction, fold-specific preprocessing, model settings, and bootstrap procedure from those files. Do not infer missing settings from rounded results.

For an independent check, start a clean runtime, run all stages without cached intermediate results, and confirm that training and testing participant IDs never overlap. Write new outputs to a separate directory. Run:

```sh
python3 tools/check_summary.py /path/to/new/run/Final_key_statistics.csv
```

Input: the original export format with columns `statistic,value`. Counts must match exactly; the metric tolerance is 0.000001 against the six-decimal reported export. A passing check establishes numerical agreement only. Record the environment, command, input versions and discrepancies alongside any claimed reproduction.
