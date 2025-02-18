import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TimeSeriesForecast_COTReport_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TimeSeriesForecast und COTReport
    """
    
    params = (
        ('indicators', {
            'TimeSeriesForecast': {
                'class': TimeSeriesForecast,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeSeriesForecast'>
            },
            'COTReport': {
                'class': COTReport,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_COTReport'>
            }
        }),
        ('weights', {
            'TimeSeriesForecast': 1.0,
            'COTReport': 1.0
        })
    )
