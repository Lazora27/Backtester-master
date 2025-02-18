import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PriceDelta_DonchianChannels_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PriceDelta und DonchianChannels
    """
    
    params = (
        ('indicators', {
            'PriceDelta': {
                'class': PriceDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceDelta'>
            },
            'DonchianChannels': {
                'class': DonchianChannels,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DonchianChannels'>
            }
        }),
        ('weights', {
            'PriceDelta': 1.0,
            'DonchianChannels': 1.0
        })
    )
