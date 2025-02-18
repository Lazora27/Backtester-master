import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RainbowMovingAverage_TRIXIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RainbowMovingAverage und TRIXIndicator
    """
    
    params = (
        ('indicators', {
            'RainbowMovingAverage': {
                'class': RainbowMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RainbowMovingAverage'>
            },
            'TRIXIndicator': {
                'class': TRIXIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TRIXIndicator'>
            }
        }),
        ('weights', {
            'RainbowMovingAverage': 1.0,
            'TRIXIndicator': 1.0
        })
    )
