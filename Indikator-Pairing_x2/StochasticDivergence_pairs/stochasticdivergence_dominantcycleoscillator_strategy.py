import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticDivergence_DominantCycleOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticDivergence und DominantCycleOscillator
    """
    
    params = (
        ('indicators', {
            'StochasticDivergence': {
                'class': StochasticDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticDivergence'>
            },
            'DominantCycleOscillator': {
                'class': DominantCycleOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DominantCycleOscillator'>
            }
        }),
        ('weights', {
            'StochasticDivergence': 1.0,
            'DominantCycleOscillator': 1.0
        })
    )
