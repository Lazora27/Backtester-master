import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ParabolicSAR_SimpleMovingAverage_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ParabolicSAR und SimpleMovingAverage
    """
    
    params = (
        ('indicators', {
            'ParabolicSAR': {
                'class': ParabolicSAR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ParabolicSAR'>
            },
            'SimpleMovingAverage': {
                'class': SimpleMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SimpleMovingAverage'>
            }
        }),
        ('weights', {
            'ParabolicSAR': 1.0,
            'SimpleMovingAverage': 1.0
        })
    )
