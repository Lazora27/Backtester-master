import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WilliamsR_KeltnerChannels_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WilliamsR und KeltnerChannels
    """
    
    params = (
        ('indicators', {
            'WilliamsR': {
                'class': WilliamsR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WilliamsR1'>
            },
            'KeltnerChannels': {
                'class': KeltnerChannels,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KeltnerChannels'>
            }
        }),
        ('weights', {
            'WilliamsR': 1.0,
            'KeltnerChannels': 1.0
        })
    )
