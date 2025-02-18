import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TrendExhaustion_KeltnerChannels_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TrendExhaustion und KeltnerChannels
    """
    
    params = (
        ('indicators', {
            'TrendExhaustion': {
                'class': TrendExhaustion,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrendExhaustion'>
            },
            'KeltnerChannels': {
                'class': KeltnerChannels,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KeltnerChannels'>
            }
        }),
        ('weights', {
            'TrendExhaustion': 1.0,
            'KeltnerChannels': 1.0
        })
    )
