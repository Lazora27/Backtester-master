import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SimpleMovingAverage_AccelerationBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SimpleMovingAverage und AccelerationBands
    """
    
    params = (
        ('indicators', {
            'SimpleMovingAverage': {
                'class': SimpleMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SimpleMovingAverage'>
            },
            'AccelerationBands': {
                'class': AccelerationBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AccelerationBands'>
            }
        }),
        ('weights', {
            'SimpleMovingAverage': 1.0,
            'AccelerationBands': 1.0
        })
    )
