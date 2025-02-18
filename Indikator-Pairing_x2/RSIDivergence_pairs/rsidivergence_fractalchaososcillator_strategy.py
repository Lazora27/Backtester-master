import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RSIDivergence_FractalChaosOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RSIDivergence und FractalChaosOscillator
    """
    
    params = (
        ('indicators', {
            'RSIDivergence': {
                'class': RSIDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RSIDivergence'>
            },
            'FractalChaosOscillator': {
                'class': FractalChaosOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FractalChaosOscillator'>
            }
        }),
        ('weights', {
            'RSIDivergence': 1.0,
            'FractalChaosOscillator': 1.0
        })
    )
