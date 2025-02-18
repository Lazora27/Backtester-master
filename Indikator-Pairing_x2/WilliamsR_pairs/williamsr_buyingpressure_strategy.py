import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WilliamsR_BuyingPressure_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WilliamsR und BuyingPressure
    """
    
    params = (
        ('indicators', {
            'WilliamsR': {
                'class': WilliamsR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WilliamsR1'>
            },
            'BuyingPressure': {
                'class': BuyingPressure,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BuyingPressure'>
            }
        }),
        ('weights', {
            'WilliamsR': 1.0,
            'BuyingPressure': 1.0
        })
    )
