import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MovingAverage_AdaptiveATR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MovingAverage und AdaptiveATR
    """
    
    params = (
        ('indicators', {
            'MovingAverage': {
                'class': MovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MovingAverage'>
            },
            'AdaptiveATR': {
                'class': AdaptiveATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveATR'>
            }
        }),
        ('weights', {
            'MovingAverage': 1.0,
            'AdaptiveATR': 1.0
        })
    )
