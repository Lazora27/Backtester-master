import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticDivergence_FractalChaosOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticDivergence und FractalChaosOscillator
    """
    
    params = (
        ('indicators', {
            'StochasticDivergence': {
                'class': StochasticDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticDivergence'>
            },
            'FractalChaosOscillator': {
                'class': FractalChaosOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FractalChaosOscillator'>
            }
        }),
        ('weights', {
            'StochasticDivergence': 1.0,
            'FractalChaosOscillator': 1.0
        })
    )
