import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MovingAverage_AverageLogRange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MovingAverage und AverageLogRange
    """
    
    params = (
        ('indicators', {
            'MovingAverage': {
                'class': MovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MovingAverage'>
            },
            'AverageLogRange': {
                'class': AverageLogRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageLogRange'>
            }
        }),
        ('weights', {
            'MovingAverage': 1.0,
            'AverageLogRange': 1.0
        })
    )
