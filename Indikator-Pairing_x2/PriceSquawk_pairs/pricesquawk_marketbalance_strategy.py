import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PriceSquawk_MarketBalance_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PriceSquawk und MarketBalance
    """
    
    params = (
        ('indicators', {
            'PriceSquawk': {
                'class': PriceSquawk,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceSquawk'>
            },
            'MarketBalance': {
                'class': MarketBalance,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketBalance'>
            }
        }),
        ('weights', {
            'PriceSquawk': 1.0,
            'MarketBalance': 1.0
        })
    )
