import backtrader as bt
from ..base_strategy import FlexibleStrategy

class COTReport_WeightedMovingAverage_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von COTReport und WeightedMovingAverage
    """
    
    params = (
        ('indicators', {
            'COTReport': {
                'class': COTReport,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_COTReport'>
            },
            'WeightedMovingAverage': {
                'class': WeightedMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeightedMovingAverage'>
            }
        }),
        ('weights', {
            'COTReport': 1.0,
            'WeightedMovingAverage': 1.0
        })
    )
