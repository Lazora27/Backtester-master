import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SimpleMovingAverage_TrueRange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SimpleMovingAverage und TrueRange
    """
    
    params = (
        ('indicators', {
            'SimpleMovingAverage': {
                'class': SimpleMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SimpleMovingAverage'>
            },
            'TrueRange': {
                'class': TrueRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrueRange1'>
            }
        }),
        ('weights', {
            'SimpleMovingAverage': 1.0,
            'TrueRange': 1.0
        })
    )
