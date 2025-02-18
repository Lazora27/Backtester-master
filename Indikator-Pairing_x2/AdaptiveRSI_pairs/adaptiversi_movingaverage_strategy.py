import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AdaptiveRSI_MovingAverage_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AdaptiveRSI und MovingAverage
    """
    
    params = (
        ('indicators', {
            'AdaptiveRSI': {
                'class': AdaptiveRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveRSI'>
            },
            'MovingAverage': {
                'class': MovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MovingAverage'>
            }
        }),
        ('weights', {
            'AdaptiveRSI': 1.0,
            'MovingAverage': 1.0
        })
    )
