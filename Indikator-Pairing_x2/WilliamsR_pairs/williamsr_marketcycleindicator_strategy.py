import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WilliamsR_MarketCycleIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WilliamsR und MarketCycleIndicator
    """
    
    params = (
        ('indicators', {
            'WilliamsR': {
                'class': WilliamsR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WilliamsR1'>
            },
            'MarketCycleIndicator': {
                'class': MarketCycleIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketCycleIndicator'>
            }
        }),
        ('weights', {
            'WilliamsR': 1.0,
            'MarketCycleIndicator': 1.0
        })
    )
