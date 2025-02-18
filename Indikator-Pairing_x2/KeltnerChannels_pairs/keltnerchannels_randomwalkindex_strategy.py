import backtrader as bt
from ..base_strategy import FlexibleStrategy

class KeltnerChannels_RandomWalkIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von KeltnerChannels und RandomWalkIndex
    """
    
    params = (
        ('indicators', {
            'KeltnerChannels': {
                'class': KeltnerChannels,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KeltnerChannels'>
            },
            'RandomWalkIndex': {
                'class': RandomWalkIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RandomWalkIndex'>
            }
        }),
        ('weights', {
            'KeltnerChannels': 1.0,
            'RandomWalkIndex': 1.0
        })
    )
