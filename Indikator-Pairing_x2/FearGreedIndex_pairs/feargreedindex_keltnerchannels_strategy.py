import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FearGreedIndex_KeltnerChannels_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FearGreedIndex und KeltnerChannels
    """
    
    params = (
        ('indicators', {
            'FearGreedIndex': {
                'class': FearGreedIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FearGreedIndex'>
            },
            'KeltnerChannels': {
                'class': KeltnerChannels,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KeltnerChannels'>
            }
        }),
        ('weights', {
            'FearGreedIndex': 1.0,
            'KeltnerChannels': 1.0
        })
    )
