import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WilliamsR_MarketBalance_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WilliamsR und MarketBalance
    """
    
    params = (
        ('indicators', {
            'WilliamsR': {
                'class': WilliamsR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WilliamsR1'>
            },
            'MarketBalance': {
                'class': MarketBalance,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketBalance'>
            }
        }),
        ('weights', {
            'WilliamsR': 1.0,
            'MarketBalance': 1.0
        })
    )
