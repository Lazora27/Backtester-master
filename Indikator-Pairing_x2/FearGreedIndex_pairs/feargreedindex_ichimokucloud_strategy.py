import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FearGreedIndex_IchimokuCloud_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FearGreedIndex und IchimokuCloud
    """
    
    params = (
        ('indicators', {
            'FearGreedIndex': {
                'class': FearGreedIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FearGreedIndex'>
            },
            'IchimokuCloud': {
                'class': IchimokuCloud,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_IchimokuCloud'>
            }
        }),
        ('weights', {
            'FearGreedIndex': 1.0,
            'IchimokuCloud': 1.0
        })
    )
