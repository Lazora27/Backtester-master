import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PriceDelta_KeltnerChannels_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PriceDelta und KeltnerChannels
    """
    
    params = (
        ('indicators', {
            'PriceDelta': {
                'class': PriceDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceDelta'>
            },
            'KeltnerChannels': {
                'class': KeltnerChannels,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KeltnerChannels'>
            }
        }),
        ('weights', {
            'PriceDelta': 1.0,
            'KeltnerChannels': 1.0
        })
    )
