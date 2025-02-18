import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ParabolicSAR_RainbowMovingAverage_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ParabolicSAR und RainbowMovingAverage
    """
    
    params = (
        ('indicators', {
            'ParabolicSAR': {
                'class': ParabolicSAR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ParabolicSAR'>
            },
            'RainbowMovingAverage': {
                'class': RainbowMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RainbowMovingAverage'>
            }
        }),
        ('weights', {
            'ParabolicSAR': 1.0,
            'RainbowMovingAverage': 1.0
        })
    )
