import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MarketOrderFlow_DonchianChannels_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MarketOrderFlow und DonchianChannels
    """
    
    params = (
        ('indicators', {
            'MarketOrderFlow': {
                'class': MarketOrderFlow,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketOrderFlow'>
            },
            'DonchianChannels': {
                'class': DonchianChannels,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DonchianChannels'>
            }
        }),
        ('weights', {
            'MarketOrderFlow': 1.0,
            'DonchianChannels': 1.0
        })
    )
