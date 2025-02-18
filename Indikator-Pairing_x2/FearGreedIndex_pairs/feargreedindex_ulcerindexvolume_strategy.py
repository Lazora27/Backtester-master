import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FearGreedIndex_UlcerIndexVolume_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FearGreedIndex und UlcerIndexVolume
    """
    
    params = (
        ('indicators', {
            'FearGreedIndex': {
                'class': FearGreedIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FearGreedIndex'>
            },
            'UlcerIndexVolume': {
                'class': UlcerIndexVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_UlcerIndexVolume'>
            }
        }),
        ('weights', {
            'FearGreedIndex': 1.0,
            'UlcerIndexVolume': 1.0
        })
    )
