import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CumulativeTick_DonchianChannels_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CumulativeTick und DonchianChannels
    """
    
    params = (
        ('indicators', {
            'CumulativeTick': {
                'class': CumulativeTick,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CumulativeTick'>
            },
            'DonchianChannels': {
                'class': DonchianChannels,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DonchianChannels'>
            }
        }),
        ('weights', {
            'CumulativeTick': 1.0,
            'DonchianChannels': 1.0
        })
    )
