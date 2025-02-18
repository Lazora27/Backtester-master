import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WeightedMovingAverage_BarStrength_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WeightedMovingAverage und BarStrength
    """
    
    params = (
        ('indicators', {
            'WeightedMovingAverage': {
                'class': WeightedMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeightedMovingAverage'>
            },
            'BarStrength': {
                'class': BarStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BarStrength'>
            }
        }),
        ('weights', {
            'WeightedMovingAverage': 1.0,
            'BarStrength': 1.0
        })
    )
