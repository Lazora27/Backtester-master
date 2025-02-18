import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WilliamsR_MarketOrderFlow_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WilliamsR und MarketOrderFlow
    """
    
    params = (
        ('indicators', {
            'WilliamsR': {
                'class': WilliamsR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WilliamsR1'>
            },
            'MarketOrderFlow': {
                'class': MarketOrderFlow,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketOrderFlow'>
            }
        }),
        ('weights', {
            'WilliamsR': 1.0,
            'MarketOrderFlow': 1.0
        })
    )
