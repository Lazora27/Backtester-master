import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MLForecast_COTReport_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MLForecast und COTReport
    """
    
    params = (
        ('indicators', {
            'MLForecast': {
                'class': MLForecast,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MLForecast'>
            },
            'COTReport': {
                'class': COTReport,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_COTReport'>
            }
        }),
        ('weights', {
            'MLForecast': 1.0,
            'COTReport': 1.0
        })
    )
