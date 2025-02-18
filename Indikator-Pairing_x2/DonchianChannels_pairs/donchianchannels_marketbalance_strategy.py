import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DonchianChannels_MarketBalance_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DonchianChannels und MarketBalance
    """
    
    params = (
        ('indicators', {
            'DonchianChannels': {
                'class': DonchianChannels,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DonchianChannels'>
            },
            'MarketBalance': {
                'class': MarketBalance,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketBalance'>
            }
        }),
        ('weights', {
            'DonchianChannels': 1.0,
            'MarketBalance': 1.0
        })
    )
