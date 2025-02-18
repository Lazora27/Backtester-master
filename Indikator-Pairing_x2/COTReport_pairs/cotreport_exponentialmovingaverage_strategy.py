import backtrader as bt
from ..base_strategy import FlexibleStrategy

class COTReport_ExponentialMovingAverage_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von COTReport und ExponentialMovingAverage
    """
    
    params = (
        ('indicators', {
            'COTReport': {
                'class': COTReport,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_COTReport'>
            },
            'ExponentialMovingAverage': {
                'class': ExponentialMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ExponentialMovingAverage'>
            }
        }),
        ('weights', {
            'COTReport': 1.0,
            'ExponentialMovingAverage': 1.0
        })
    )
