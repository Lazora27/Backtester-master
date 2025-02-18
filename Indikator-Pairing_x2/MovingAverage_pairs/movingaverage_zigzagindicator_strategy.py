import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MovingAverage_ZigZagIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MovingAverage und ZigZagIndicator
    """
    
    params = (
        ('indicators', {
            'MovingAverage': {
                'class': MovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MovingAverage'>
            },
            'ZigZagIndicator': {
                'class': ZigZagIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ZigZagIndicator'>
            }
        }),
        ('weights', {
            'MovingAverage': 1.0,
            'ZigZagIndicator': 1.0
        })
    )
