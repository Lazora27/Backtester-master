import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FearGreedIndex_SmoothedCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FearGreedIndex und SmoothedCycle
    """
    
    params = (
        ('indicators', {
            'FearGreedIndex': {
                'class': FearGreedIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FearGreedIndex'>
            },
            'SmoothedCycle': {
                'class': SmoothedCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmoothedCycle'>
            }
        }),
        ('weights', {
            'FearGreedIndex': 1.0,
            'SmoothedCycle': 1.0
        })
    )
