import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SimpleMovingAverage_FourierCycleFilter_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SimpleMovingAverage und FourierCycleFilter
    """
    
    params = (
        ('indicators', {
            'SimpleMovingAverage': {
                'class': SimpleMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SimpleMovingAverage'>
            },
            'FourierCycleFilter': {
                'class': FourierCycleFilter,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FourierCycleFilter'>
            }
        }),
        ('weights', {
            'SimpleMovingAverage': 1.0,
            'FourierCycleFilter': 1.0
        })
    )
