import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CumulativeTick_KeltnerChannels_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CumulativeTick und KeltnerChannels
    """
    
    params = (
        ('indicators', {
            'CumulativeTick': {
                'class': CumulativeTick,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CumulativeTick'>
            },
            'KeltnerChannels': {
                'class': KeltnerChannels,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KeltnerChannels'>
            }
        }),
        ('weights', {
            'CumulativeTick': 1.0,
            'KeltnerChannels': 1.0
        })
    )
