import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FearGreedIndex_TrueRangeIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FearGreedIndex und TrueRangeIndicator
    """
    
    params = (
        ('indicators', {
            'FearGreedIndex': {
                'class': FearGreedIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FearGreedIndex'>
            },
            'TrueRangeIndicator': {
                'class': TrueRangeIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrueRangeIndicator'>
            }
        }),
        ('weights', {
            'FearGreedIndex': 1.0,
            'TrueRangeIndicator': 1.0
        })
    )
