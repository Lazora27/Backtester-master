import backtrader as bt
from ..base_strategy import FlexibleStrategy

class COTReport_HullMovingAverage_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von COTReport und HullMovingAverage
    """
    
    params = (
        ('indicators', {
            'COTReport': {
                'class': COTReport,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_COTReport'>
            },
            'HullMovingAverage': {
                'class': HullMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HullMovingAverage'>
            }
        }),
        ('weights', {
            'COTReport': 1.0,
            'HullMovingAverage': 1.0
        })
    )
