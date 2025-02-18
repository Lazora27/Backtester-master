import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HighLowIndex_ExponentialMovingAverage_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HighLowIndex und ExponentialMovingAverage
    """
    
    params = (
        ('indicators', {
            'HighLowIndex': {
                'class': HighLowIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HighLowIndex'>
            },
            'ExponentialMovingAverage': {
                'class': ExponentialMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ExponentialMovingAverage'>
            }
        }),
        ('weights', {
            'HighLowIndex': 1.0,
            'ExponentialMovingAverage': 1.0
        })
    )
