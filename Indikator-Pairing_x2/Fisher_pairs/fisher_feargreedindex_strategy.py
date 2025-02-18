import backtrader as bt
from ..base_strategy import FlexibleStrategy

class Fisher_FearGreedIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von Fisher und FearGreedIndex
    """
    
    params = (
        ('indicators', {
            'Fisher': {
                'class': Fisher,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_Fisher'>
            },
            'FearGreedIndex': {
                'class': FearGreedIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FearGreedIndex'>
            }
        }),
        ('weights', {
            'Fisher': 1.0,
            'FearGreedIndex': 1.0
        })
    )
