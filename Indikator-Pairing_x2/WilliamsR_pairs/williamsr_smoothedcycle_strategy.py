import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WilliamsR_SmoothedCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WilliamsR und SmoothedCycle
    """
    
    params = (
        ('indicators', {
            'WilliamsR': {
                'class': WilliamsR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WilliamsR1'>
            },
            'SmoothedCycle': {
                'class': SmoothedCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmoothedCycle'>
            }
        }),
        ('weights', {
            'WilliamsR': 1.0,
            'SmoothedCycle': 1.0
        })
    )
