import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PivotPoints_FearGreedIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PivotPoints und FearGreedIndex
    """
    
    params = (
        ('indicators', {
            'PivotPoints': {
                'class': PivotPoints,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PivotPoints'>
            },
            'FearGreedIndex': {
                'class': FearGreedIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FearGreedIndex'>
            }
        }),
        ('weights', {
            'PivotPoints': 1.0,
            'FearGreedIndex': 1.0
        })
    )
