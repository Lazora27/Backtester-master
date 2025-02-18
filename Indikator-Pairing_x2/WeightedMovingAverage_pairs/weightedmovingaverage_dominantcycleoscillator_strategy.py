import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WeightedMovingAverage_DominantCycleOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WeightedMovingAverage und DominantCycleOscillator
    """
    
    params = (
        ('indicators', {
            'WeightedMovingAverage': {
                'class': WeightedMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeightedMovingAverage'>
            },
            'DominantCycleOscillator': {
                'class': DominantCycleOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DominantCycleOscillator'>
            }
        }),
        ('weights', {
            'WeightedMovingAverage': 1.0,
            'DominantCycleOscillator': 1.0
        })
    )
