import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DonchianChannels_MarketCycleIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DonchianChannels und MarketCycleIndicator
    """
    
    params = (
        ('indicators', {
            'DonchianChannels': {
                'class': DonchianChannels,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DonchianChannels'>
            },
            'MarketCycleIndicator': {
                'class': MarketCycleIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketCycleIndicator'>
            }
        }),
        ('weights', {
            'DonchianChannels': 1.0,
            'MarketCycleIndicator': 1.0
        })
    )
