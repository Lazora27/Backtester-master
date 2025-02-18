import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticRSI_FearGreedIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticRSI und FearGreedIndex
    """
    
    params = (
        ('indicators', {
            'StochasticRSI': {
                'class': StochasticRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticRSI'>
            },
            'FearGreedIndex': {
                'class': FearGreedIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FearGreedIndex'>
            }
        }),
        ('weights', {
            'StochasticRSI': 1.0,
            'FearGreedIndex': 1.0
        })
    )
