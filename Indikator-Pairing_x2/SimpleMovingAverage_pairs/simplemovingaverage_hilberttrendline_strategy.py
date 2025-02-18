import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SimpleMovingAverage_HilbertTrendline_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SimpleMovingAverage und HilbertTrendline
    """
    
    params = (
        ('indicators', {
            'SimpleMovingAverage': {
                'class': SimpleMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SimpleMovingAverage'>
            },
            'HilbertTrendline': {
                'class': HilbertTrendline,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertTrendline'>
            }
        }),
        ('weights', {
            'SimpleMovingAverage': 1.0,
            'HilbertTrendline': 1.0
        })
    )
