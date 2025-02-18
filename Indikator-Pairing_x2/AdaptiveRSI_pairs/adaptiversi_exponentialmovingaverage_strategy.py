import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AdaptiveRSI_ExponentialMovingAverage_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AdaptiveRSI und ExponentialMovingAverage
    """
    
    params = (
        ('indicators', {
            'AdaptiveRSI': {
                'class': AdaptiveRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveRSI'>
            },
            'ExponentialMovingAverage': {
                'class': ExponentialMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ExponentialMovingAverage'>
            }
        }),
        ('weights', {
            'AdaptiveRSI': 1.0,
            'ExponentialMovingAverage': 1.0
        })
    )
