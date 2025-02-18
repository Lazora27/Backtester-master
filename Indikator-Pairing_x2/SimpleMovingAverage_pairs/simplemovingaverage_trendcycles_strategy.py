import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SimpleMovingAverage_TrendCycles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SimpleMovingAverage und TrendCycles
    """
    
    params = (
        ('indicators', {
            'SimpleMovingAverage': {
                'class': SimpleMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SimpleMovingAverage'>
            },
            'TrendCycles': {
                'class': TrendCycles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrendCycles'>
            }
        }),
        ('weights', {
            'SimpleMovingAverage': 1.0,
            'TrendCycles': 1.0
        })
    )
