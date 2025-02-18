import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MovingAverage_HilbertTrendline_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MovingAverage und HilbertTrendline
    """
    
    params = (
        ('indicators', {
            'MovingAverage': {
                'class': MovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MovingAverage'>
            },
            'HilbertTrendline': {
                'class': HilbertTrendline,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertTrendline'>
            }
        }),
        ('weights', {
            'MovingAverage': 1.0,
            'HilbertTrendline': 1.0
        })
    )
