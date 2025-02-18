import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FractalChaosOscillator_CumulativeTick_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FractalChaosOscillator und CumulativeTick
    """
    
    params = (
        ('indicators', {
            'FractalChaosOscillator': {
                'class': FractalChaosOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FractalChaosOscillator'>
            },
            'CumulativeTick': {
                'class': CumulativeTick,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CumulativeTick'>
            }
        }),
        ('weights', {
            'FractalChaosOscillator': 1.0,
            'CumulativeTick': 1.0
        })
    )
