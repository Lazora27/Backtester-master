import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WilliamsR_SimpleMovingAverage_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WilliamsR und SimpleMovingAverage
    """
    
    params = (
        ('indicators', {
            'WilliamsR': {
                'class': WilliamsR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WilliamsR1'>
            },
            'SimpleMovingAverage': {
                'class': SimpleMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SimpleMovingAverage'>
            }
        }),
        ('weights', {
            'WilliamsR': 1.0,
            'SimpleMovingAverage': 1.0
        })
    )
