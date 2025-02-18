import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FearGreedIndex_DonchianChannels_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FearGreedIndex und DonchianChannels
    """
    
    params = (
        ('indicators', {
            'FearGreedIndex': {
                'class': FearGreedIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FearGreedIndex'>
            },
            'DonchianChannels': {
                'class': DonchianChannels,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DonchianChannels'>
            }
        }),
        ('weights', {
            'FearGreedIndex': 1.0,
            'DonchianChannels': 1.0
        })
    )
