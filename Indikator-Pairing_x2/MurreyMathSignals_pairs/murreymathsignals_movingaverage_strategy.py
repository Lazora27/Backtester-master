import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MurreyMathSignals_MovingAverage_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MurreyMathSignals und MovingAverage
    """
    
    params = (
        ('indicators', {
            'MurreyMathSignals': {
                'class': MurreyMathSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MurreyMathSignals'>
            },
            'MovingAverage': {
                'class': MovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MovingAverage'>
            }
        }),
        ('weights', {
            'MurreyMathSignals': 1.0,
            'MovingAverage': 1.0
        })
    )
