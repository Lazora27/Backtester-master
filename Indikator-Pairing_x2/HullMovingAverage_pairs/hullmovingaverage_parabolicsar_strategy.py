import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HullMovingAverage_ParabolicSAR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HullMovingAverage und ParabolicSAR
    """
    
    params = (
        ('indicators', {
            'HullMovingAverage': {
                'class': HullMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HullMovingAverage'>
            },
            'ParabolicSAR': {
                'class': ParabolicSAR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ParabolicSAR'>
            }
        }),
        ('weights', {
            'HullMovingAverage': 1.0,
            'ParabolicSAR': 1.0
        })
    )
