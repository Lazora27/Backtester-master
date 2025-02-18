import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MovingAverage_TrueRangeIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MovingAverage und TrueRangeIndicator
    """
    
    params = (
        ('indicators', {
            'MovingAverage': {
                'class': MovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MovingAverage'>
            },
            'TrueRangeIndicator': {
                'class': TrueRangeIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrueRangeIndicator'>
            }
        }),
        ('weights', {
            'MovingAverage': 1.0,
            'TrueRangeIndicator': 1.0
        })
    )
