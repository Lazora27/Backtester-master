import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AdaptiveRSI_RainbowMovingAverage_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AdaptiveRSI und RainbowMovingAverage
    """
    
    params = (
        ('indicators', {
            'AdaptiveRSI': {
                'class': AdaptiveRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveRSI'>
            },
            'RainbowMovingAverage': {
                'class': RainbowMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RainbowMovingAverage'>
            }
        }),
        ('weights', {
            'AdaptiveRSI': 1.0,
            'RainbowMovingAverage': 1.0
        })
    )
