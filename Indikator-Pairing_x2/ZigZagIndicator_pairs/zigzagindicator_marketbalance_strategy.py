import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ZigZagIndicator_MarketBalance_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ZigZagIndicator und MarketBalance
    """
    
    params = (
        ('indicators', {
            'ZigZagIndicator': {
                'class': ZigZagIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ZigZagIndicator'>
            },
            'MarketBalance': {
                'class': MarketBalance,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketBalance'>
            }
        }),
        ('weights', {
            'ZigZagIndicator': 1.0,
            'MarketBalance': 1.0
        })
    )
