import backtrader as bt
from ..base_strategy import FlexibleStrategy

class Fisher_ExponentialMovingAverage_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von Fisher und ExponentialMovingAverage
    """
    
    params = (
        ('indicators', {
            'Fisher': {
                'class': Fisher,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_Fisher'>
            },
            'ExponentialMovingAverage': {
                'class': ExponentialMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ExponentialMovingAverage'>
            }
        }),
        ('weights', {
            'Fisher': 1.0,
            'ExponentialMovingAverage': 1.0
        })
    )
