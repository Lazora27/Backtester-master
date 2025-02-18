import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FractalChaosOscillator_WeightedMovingAverage_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FractalChaosOscillator und WeightedMovingAverage
    """
    
    params = (
        ('indicators', {
            'FractalChaosOscillator': {
                'class': FractalChaosOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FractalChaosOscillator'>
            },
            'WeightedMovingAverage': {
                'class': WeightedMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeightedMovingAverage'>
            }
        }),
        ('weights', {
            'FractalChaosOscillator': 1.0,
            'WeightedMovingAverage': 1.0
        })
    )
