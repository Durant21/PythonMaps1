from dateutil.parser import parse

from PythonMaps1.viewmodels.PythonMaps.create_ts_viewmodel import CreateTSViewModel


class UpdateTSViewModel( CreateTSViewModel ):
    def __init__(self, data_dict, ts_id):
        super().__init__(data_dict)
        self.ts_id = ts_id

    def compute_details(self):

        ts_id = self.data_dict.get('ts_id')
        if not self.ts_id:
            self.errors.append("No timeseries ID specified.")
        if self.ts_id != ts_id:
            self.errors.append("Timeseries ID mismatch.")

        super().compute_details()