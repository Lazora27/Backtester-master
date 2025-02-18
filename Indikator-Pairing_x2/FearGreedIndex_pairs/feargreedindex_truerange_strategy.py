import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FearGreedIndex_TrueRange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FearGreedIndex und TrueRange
    """
    
    params = (
        ('indicators', {
            'FearGreedIndex': {
                'class': FearGreedIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FearGreedIndex'>
            },
            'TrueRange': {
                'class': TrueRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrueRange1'>
            }
        }),
        ('weights', {
            'FearGreedIndex': 1.0,
            'TrueRange': 1.0
        })
    )
