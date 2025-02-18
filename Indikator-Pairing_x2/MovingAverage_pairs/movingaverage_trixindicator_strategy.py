import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MovingAverage_TRIXIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MovingAverage und TRIXIndicator
    """
    
    params = (
        ('indicators', {
            'MovingAverage': {
                'class': MovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MovingAverage'>
            },
            'TRIXIndicator': {
                'class': TRIXIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TRIXIndicator'>
            }
        }),
        ('weights', {
            'MovingAverage': 1.0,
            'TRIXIndicator': 1.0
        })
    )
