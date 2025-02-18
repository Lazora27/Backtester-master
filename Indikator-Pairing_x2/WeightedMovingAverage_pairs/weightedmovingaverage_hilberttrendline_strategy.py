import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WeightedMovingAverage_HilbertTrendline_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WeightedMovingAverage und HilbertTrendline
    """
    
    params = (
        ('indicators', {
            'WeightedMovingAverage': {
                'class': WeightedMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeightedMovingAverage'>
            },
            'HilbertTrendline': {
                'class': HilbertTrendline,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertTrendline'>
            }
        }),
        ('weights', {
            'WeightedMovingAverage': 1.0,
            'HilbertTrendline': 1.0
        })
    )
