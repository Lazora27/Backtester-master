import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PutCallRatio_ExponentialMovingAverage_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PutCallRatio und ExponentialMovingAverage
    """
    
    params = (
        ('indicators', {
            'PutCallRatio': {
                'class': PutCallRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PutCallRatio1'>
            },
            'ExponentialMovingAverage': {
                'class': ExponentialMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ExponentialMovingAverage'>
            }
        }),
        ('weights', {
            'PutCallRatio': 1.0,
            'ExponentialMovingAverage': 1.0
        })
    )
