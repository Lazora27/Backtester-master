import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SuperMACD_FearGreedIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SuperMACD und FearGreedIndex
    """
    
    params = (
        ('indicators', {
            'SuperMACD': {
                'class': SuperMACD,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SuperMACD'>
            },
            'FearGreedIndex': {
                'class': FearGreedIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FearGreedIndex'>
            }
        }),
        ('weights', {
            'SuperMACD': 1.0,
            'FearGreedIndex': 1.0
        })
    )
