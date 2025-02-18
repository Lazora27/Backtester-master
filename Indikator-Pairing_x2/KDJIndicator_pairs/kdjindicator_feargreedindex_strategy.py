import backtrader as bt
from ..base_strategy import FlexibleStrategy

class KDJIndicator_FearGreedIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von KDJIndicator und FearGreedIndex
    """
    
    params = (
        ('indicators', {
            'KDJIndicator': {
                'class': KDJIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KDJIndicator'>
            },
            'FearGreedIndex': {
                'class': FearGreedIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FearGreedIndex'>
            }
        }),
        ('weights', {
            'KDJIndicator': 1.0,
            'FearGreedIndex': 1.0
        })
    )
