import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FearGreedIndex_WeightedCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FearGreedIndex und WeightedCycle
    """
    
    params = (
        ('indicators', {
            'FearGreedIndex': {
                'class': FearGreedIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FearGreedIndex'>
            },
            'WeightedCycle': {
                'class': WeightedCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeightedCycle'>
            }
        }),
        ('weights', {
            'FearGreedIndex': 1.0,
            'WeightedCycle': 1.0
        })
    )
