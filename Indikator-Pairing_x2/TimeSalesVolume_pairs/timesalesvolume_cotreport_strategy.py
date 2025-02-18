import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TimeSalesVolume_COTReport_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TimeSalesVolume und COTReport
    """
    
    params = (
        ('indicators', {
            'TimeSalesVolume': {
                'class': TimeSalesVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeSalesVolume'>
            },
            'COTReport': {
                'class': COTReport,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_COTReport'>
            }
        }),
        ('weights', {
            'TimeSalesVolume': 1.0,
            'COTReport': 1.0
        })
    )
