import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ParabolicSAR_WeightedMovingAverage_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ParabolicSAR und WeightedMovingAverage
    """
    
    params = (
        ('indicators', {
            'ParabolicSAR': {
                'class': ParabolicSAR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ParabolicSAR'>
            },
            'WeightedMovingAverage': {
                'class': WeightedMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeightedMovingAverage'>
            }
        }),
        ('weights', {
            'ParabolicSAR': 1.0,
            'WeightedMovingAverage': 1.0
        })
    )
