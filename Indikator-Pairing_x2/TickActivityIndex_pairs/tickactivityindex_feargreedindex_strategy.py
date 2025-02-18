import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TickActivityIndex_FearGreedIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TickActivityIndex und FearGreedIndex
    """
    
    params = (
        ('indicators', {
            'TickActivityIndex': {
                'class': TickActivityIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickActivityIndex'>
            },
            'FearGreedIndex': {
                'class': FearGreedIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FearGreedIndex'>
            }
        }),
        ('weights', {
            'TickActivityIndex': 1.0,
            'FearGreedIndex': 1.0
        })
    )
