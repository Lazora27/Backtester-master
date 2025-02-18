import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ExponentialMovingAverage_BarStrength_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ExponentialMovingAverage und BarStrength
    """
    
    params = (
        ('indicators', {
            'ExponentialMovingAverage': {
                'class': ExponentialMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ExponentialMovingAverage'>
            },
            'BarStrength': {
                'class': BarStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BarStrength'>
            }
        }),
        ('weights', {
            'ExponentialMovingAverage': 1.0,
            'BarStrength': 1.0
        })
    )
