import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BuyingPressure_MarketBalance_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BuyingPressure und MarketBalance
    """
    
    params = (
        ('indicators', {
            'BuyingPressure': {
                'class': BuyingPressure,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BuyingPressure'>
            },
            'MarketBalance': {
                'class': MarketBalance,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketBalance'>
            }
        }),
        ('weights', {
            'BuyingPressure': 1.0,
            'MarketBalance': 1.0
        })
    )
