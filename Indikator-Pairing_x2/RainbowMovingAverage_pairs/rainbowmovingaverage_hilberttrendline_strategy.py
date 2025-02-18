import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RainbowMovingAverage_HilbertTrendline_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RainbowMovingAverage und HilbertTrendline
    """
    
    params = (
        ('indicators', {
            'RainbowMovingAverage': {
                'class': RainbowMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RainbowMovingAverage'>
            },
            'HilbertTrendline': {
                'class': HilbertTrendline,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertTrendline'>
            }
        }),
        ('weights', {
            'RainbowMovingAverage': 1.0,
            'HilbertTrendline': 1.0
        })
    )
