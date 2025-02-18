import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ExponentialMovingAverage_EhlersDecycler_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ExponentialMovingAverage und EhlersDecycler
    """
    
    params = (
        ('indicators', {
            'ExponentialMovingAverage': {
                'class': ExponentialMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ExponentialMovingAverage'>
            },
            'EhlersDecycler': {
                'class': EhlersDecycler,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EhlersDecycler'>
            }
        }),
        ('weights', {
            'ExponentialMovingAverage': 1.0,
            'EhlersDecycler': 1.0
        })
    )
