import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ExponentialMovingAverage_ParabolicTimePrice_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ExponentialMovingAverage und ParabolicTimePrice
    """
    
    params = (
        ('indicators', {
            'ExponentialMovingAverage': {
                'class': ExponentialMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ExponentialMovingAverage'>
            },
            'ParabolicTimePrice': {
                'class': ParabolicTimePrice,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ParabolicTimePrice'>
            }
        }),
        ('weights', {
            'ExponentialMovingAverage': 1.0,
            'ParabolicTimePrice': 1.0
        })
    )
