import backtrader as bt
from ..base_strategy import FlexibleStrategy

class COTReport_AverageLogRange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von COTReport und AverageLogRange
    """
    
    params = (
        ('indicators', {
            'COTReport': {
                'class': COTReport,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_COTReport'>
            },
            'AverageLogRange': {
                'class': AverageLogRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageLogRange'>
            }
        }),
        ('weights', {
            'COTReport': 1.0,
            'AverageLogRange': 1.0
        })
    )
