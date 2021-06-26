import os
import pprint

pp = pprint.PrettyPrinter(indent=2)

import click
import datadog
from datadog import api

options = {
  'api_key': os.getenv('DATADOG_API_KEY'),
  'app_key': os.getenv('DATADOG_APPLICATION_KEY')
}
datadog.initialize(**options)

@click.command()
@click.argument("metric")
def find_metric(metric):
  """Find widgets and dashboards in your datadog setup that reference the given metric

  METRIC is the metric name to search for, eg. my_prefix.my_metric
  """
  dashboards = api.Dashboard.get_all()['dashboards']

  for dashboard in dashboards:
    dashboard_id = dashboard['id']
    full_dashboard = api.Dashboard.get(dashboard_id)
    widgets = full_dashboard['widgets']
    for widget in widgets:
      widget_definition_string = pp.pformat(widget['definition'])
      if metric in widget_definition_string:
        widget_title = widget['definition'].get('title', '<unknown>')
        dashboard_title = dashboard.get('title', '<unknown>')
        print(f"Found {metric} in the definition of widget {widget_title} in dashboard {dashboard_title}")

if __name__ == '__main__':
  find_metric()
