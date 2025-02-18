import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WilliamsR_MovingAverage_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WilliamsR und MovingAverage
    """
    
    params = (
        ('indicators', {
            'WilliamsR': {
                'class': WilliamsR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WilliamsR1'>
            },
            'MovingAverage': {
                'class': MovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MovingAverage'>
            }
        }),
        ('weights', {
            'WilliamsR': 1.0,
            'MovingAverage': 1.0
        })
    )
