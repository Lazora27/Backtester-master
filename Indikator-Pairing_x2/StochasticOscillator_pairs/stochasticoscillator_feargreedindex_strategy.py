import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticOscillator_FearGreedIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticOscillator und FearGreedIndex
    """
    
    params = (
        ('indicators', {
            'StochasticOscillator': {
                'class': StochasticOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticOscillator'>
            },
            'FearGreedIndex': {
                'class': FearGreedIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FearGreedIndex'>
            }
        }),
        ('weights', {
            'StochasticOscillator': 1.0,
            'FearGreedIndex': 1.0
        })
    )
