import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PriceDelta_MarketBalance_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PriceDelta und MarketBalance
    """
    
    params = (
        ('indicators', {
            'PriceDelta': {
                'class': PriceDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceDelta'>
            },
            'MarketBalance': {
                'class': MarketBalance,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketBalance'>
            }
        }),
        ('weights', {
            'PriceDelta': 1.0,
            'MarketBalance': 1.0
        })
    )
