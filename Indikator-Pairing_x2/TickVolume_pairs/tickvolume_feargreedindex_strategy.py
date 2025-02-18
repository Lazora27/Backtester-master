import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TickVolume_FearGreedIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TickVolume und FearGreedIndex
    """
    
    params = (
        ('indicators', {
            'TickVolume': {
                'class': TickVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickVolume'>
            },
            'FearGreedIndex': {
                'class': FearGreedIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FearGreedIndex'>
            }
        }),
        ('weights', {
            'TickVolume': 1.0,
            'FearGreedIndex': 1.0
        })
    )
