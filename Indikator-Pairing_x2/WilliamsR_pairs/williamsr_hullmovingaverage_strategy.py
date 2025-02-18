import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WilliamsR_HullMovingAverage_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WilliamsR und HullMovingAverage
    """
    
    params = (
        ('indicators', {
            'WilliamsR': {
                'class': WilliamsR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WilliamsR1'>
            },
            'HullMovingAverage': {
                'class': HullMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HullMovingAverage'>
            }
        }),
        ('weights', {
            'WilliamsR': 1.0,
            'HullMovingAverage': 1.0
        })
    )
