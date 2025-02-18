import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MovingAverage_ParabolicSAR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MovingAverage und ParabolicSAR
    """
    
    params = (
        ('indicators', {
            'MovingAverage': {
                'class': MovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MovingAverage'>
            },
            'ParabolicSAR': {
                'class': ParabolicSAR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ParabolicSAR'>
            }
        }),
        ('weights', {
            'MovingAverage': 1.0,
            'ParabolicSAR': 1.0
        })
    )
