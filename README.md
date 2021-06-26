# datadog-metric-references

Small python script to find all usages of METRIC across all widgets in all datadog dashboards

Requires env variables `DATADOG_API_KEY` and `DATADOG_APPLICATION_KEY` to be available.

## Requirements

Python 3.9.5+ and [Poetry](https://python-poetry.org/)

## Installing dependencies

```
echo 3.9.5 > .python-version
pip install --upgrade poetry==1.1.6
poetry config virtualenvs.in-project true
poetry run pip install --upgrade pip==21.1.2
poetry install --no-root
```

## Running

```
$ poetry run python find_metric_usages.py hpa.min_replicas
Found `hpa.min_replicas` in the definition of widget `Autoscaling` in dashboard `Kubernetes Service Health`
Found `hpa.min_replicas` in the definition of widget `Autoscaling` in dashboard `Kubernetes Worker Health`
...
```
