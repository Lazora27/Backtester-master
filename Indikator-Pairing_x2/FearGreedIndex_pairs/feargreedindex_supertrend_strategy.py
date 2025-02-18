import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FearGreedIndex_SuperTrend_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FearGreedIndex und SuperTrend
    """
    
    params = (
        ('indicators', {
            'FearGreedIndex': {
                'class': FearGreedIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FearGreedIndex'>
            },
            'SuperTrend': {
                'class': SuperTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SuperTrend'>
            }
        }),
        ('weights', {
            'FearGreedIndex': 1.0,
            'SuperTrend': 1.0
        })
    )
