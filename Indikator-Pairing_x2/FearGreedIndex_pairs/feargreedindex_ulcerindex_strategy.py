import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FearGreedIndex_UlcerIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FearGreedIndex und UlcerIndex
    """
    
    params = (
        ('indicators', {
            'FearGreedIndex': {
                'class': FearGreedIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FearGreedIndex'>
            },
            'UlcerIndex': {
                'class': UlcerIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_UlcerIndex'>
            }
        }),
        ('weights', {
            'FearGreedIndex': 1.0,
            'UlcerIndex': 1.0
        })
    )
