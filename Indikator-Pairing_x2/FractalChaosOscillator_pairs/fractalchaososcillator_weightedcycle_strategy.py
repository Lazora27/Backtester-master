import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FractalChaosOscillator_WeightedCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FractalChaosOscillator und WeightedCycle
    """
    
    params = (
        ('indicators', {
            'FractalChaosOscillator': {
                'class': FractalChaosOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FractalChaosOscillator'>
            },
            'WeightedCycle': {
                'class': WeightedCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeightedCycle'>
            }
        }),
        ('weights', {
            'FractalChaosOscillator': 1.0,
            'WeightedCycle': 1.0
        })
    )
