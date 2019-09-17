import pandas as pd
import numpy as np
import random
from pptx import Presentation
from pptx.enum.chart import XL_CHART_TYPE 
from pptx.chart.data import CategoryChartData

class PPT_Creator(object):
    def __init__(self):
        self._data_frames = []
    @property
    def data_frames(self):
        return self._data_frames
    def add_frame(self, df):
        self._data_frames.append(df)
    def create(self):
        """
        builds & returns the PPTX object
        """
        data_frames = self.data_frames
        p = Presentation()
        layout = p.slide_layouts[6]
        for frame in data_frames:
            cd = CategoryChartData()
            cd.categories = frame.index
            for name in frame.columns:
                cd.add_series(name, frame[name], '0%')
            slide = p.slides.add_slide( layout )
            chart_type = self._chart_type()
            shape = slide.shapes.add_chart(chart_type, 0, 0, 9143301, 6158000, cd)
        return p
    def _chart_type(self):
        """
        randomize the output format for the charts
        """
        return random.choice([
            XL_CHART_TYPE.COLUMN_CLUSTERED,
            XL_CHART_TYPE.BAR_CLUSTERED,
            ])