import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ExponentialMovingAverage_PolarizedTimePrice_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ExponentialMovingAverage und PolarizedTimePrice
    """
    
    params = (
        ('indicators', {
            'ExponentialMovingAverage': {
                'class': ExponentialMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ExponentialMovingAverage'>
            },
            'PolarizedTimePrice': {
                'class': PolarizedTimePrice,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PolarizedTimePrice'>
            }
        }),
        ('weights', {
            'ExponentialMovingAverage': 1.0,
            'PolarizedTimePrice': 1.0
        })
    )
