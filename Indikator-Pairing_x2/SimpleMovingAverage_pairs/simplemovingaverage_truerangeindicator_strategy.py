import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SimpleMovingAverage_TrueRangeIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SimpleMovingAverage und TrueRangeIndicator
    """
    
    params = (
        ('indicators', {
            'SimpleMovingAverage': {
                'class': SimpleMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SimpleMovingAverage'>
            },
            'TrueRangeIndicator': {
                'class': TrueRangeIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrueRangeIndicator'>
            }
        }),
        ('weights', {
            'SimpleMovingAverage': 1.0,
            'TrueRangeIndicator': 1.0
        })
    )
