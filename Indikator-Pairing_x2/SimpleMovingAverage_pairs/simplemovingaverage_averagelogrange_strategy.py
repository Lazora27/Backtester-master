import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SimpleMovingAverage_AverageLogRange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SimpleMovingAverage und AverageLogRange
    """
    
    params = (
        ('indicators', {
            'SimpleMovingAverage': {
                'class': SimpleMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SimpleMovingAverage'>
            },
            'AverageLogRange': {
                'class': AverageLogRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageLogRange'>
            }
        }),
        ('weights', {
            'SimpleMovingAverage': 1.0,
            'AverageLogRange': 1.0
        })
    )
