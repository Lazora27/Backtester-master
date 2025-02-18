import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RainbowMovingAverage_VortexIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RainbowMovingAverage und VortexIndicator
    """
    
    params = (
        ('indicators', {
            'RainbowMovingAverage': {
                'class': RainbowMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RainbowMovingAverage'>
            },
            'VortexIndicator': {
                'class': VortexIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VortexIndicator'>
            }
        }),
        ('weights', {
            'RainbowMovingAverage': 1.0,
            'VortexIndicator': 1.0
        })
    )
