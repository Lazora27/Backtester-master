import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WilliamsR_PriceDelta_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WilliamsR und PriceDelta
    """
    
    params = (
        ('indicators', {
            'WilliamsR': {
                'class': WilliamsR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WilliamsR1'>
            },
            'PriceDelta': {
                'class': PriceDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceDelta'>
            }
        }),
        ('weights', {
            'WilliamsR': 1.0,
            'PriceDelta': 1.0
        })
    )
