import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticDivergence_FearGreedIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticDivergence und FearGreedIndex
    """
    
    params = (
        ('indicators', {
            'StochasticDivergence': {
                'class': StochasticDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticDivergence'>
            },
            'FearGreedIndex': {
                'class': FearGreedIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FearGreedIndex'>
            }
        }),
        ('weights', {
            'StochasticDivergence': 1.0,
            'FearGreedIndex': 1.0
        })
    )
