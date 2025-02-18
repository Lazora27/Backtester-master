import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WeightedMovingAverage_ZigZagIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WeightedMovingAverage und ZigZagIndicator
    """
    
    params = (
        ('indicators', {
            'WeightedMovingAverage': {
                'class': WeightedMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeightedMovingAverage'>
            },
            'ZigZagIndicator': {
                'class': ZigZagIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ZigZagIndicator'>
            }
        }),
        ('weights', {
            'WeightedMovingAverage': 1.0,
            'ZigZagIndicator': 1.0
        })
    )
