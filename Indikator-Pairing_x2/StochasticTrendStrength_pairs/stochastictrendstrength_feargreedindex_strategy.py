import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticTrendStrength_FearGreedIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticTrendStrength und FearGreedIndex
    """
    
    params = (
        ('indicators', {
            'StochasticTrendStrength': {
                'class': StochasticTrendStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticTrendStrength'>
            },
            'FearGreedIndex': {
                'class': FearGreedIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FearGreedIndex'>
            }
        }),
        ('weights', {
            'StochasticTrendStrength': 1.0,
            'FearGreedIndex': 1.0
        })
    )
