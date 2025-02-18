import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TickIndex_FearGreedIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TickIndex und FearGreedIndex
    """
    
    params = (
        ('indicators', {
            'TickIndex': {
                'class': TickIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickIndex'>
            },
            'FearGreedIndex': {
                'class': FearGreedIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FearGreedIndex'>
            }
        }),
        ('weights', {
            'TickIndex': 1.0,
            'FearGreedIndex': 1.0
        })
    )
