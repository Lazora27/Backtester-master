import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticOscillator_DominantCycleOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticOscillator und DominantCycleOscillator
    """
    
    params = (
        ('indicators', {
            'StochasticOscillator': {
                'class': StochasticOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticOscillator'>
            },
            'DominantCycleOscillator': {
                'class': DominantCycleOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DominantCycleOscillator'>
            }
        }),
        ('weights', {
            'StochasticOscillator': 1.0,
            'DominantCycleOscillator': 1.0
        })
    )
