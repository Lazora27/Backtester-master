import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannFans_FearGreedIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannFans und FearGreedIndex
    """
    
    params = (
        ('indicators', {
            'GannFans': {
                'class': GannFans,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannFans'>
            },
            'FearGreedIndex': {
                'class': FearGreedIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FearGreedIndex'>
            }
        }),
        ('weights', {
            'GannFans': 1.0,
            'FearGreedIndex': 1.0
        })
    )
