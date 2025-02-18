import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WilliamsR_DonchianChannels_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WilliamsR und DonchianChannels
    """
    
    params = (
        ('indicators', {
            'WilliamsR': {
                'class': WilliamsR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WilliamsR1'>
            },
            'DonchianChannels': {
                'class': DonchianChannels,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DonchianChannels'>
            }
        }),
        ('weights', {
            'WilliamsR': 1.0,
            'DonchianChannels': 1.0
        })
    )
