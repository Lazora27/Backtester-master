import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MurreyMathSignals_HullMovingAverage_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MurreyMathSignals und HullMovingAverage
    """
    
    params = (
        ('indicators', {
            'MurreyMathSignals': {
                'class': MurreyMathSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MurreyMathSignals'>
            },
            'HullMovingAverage': {
                'class': HullMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HullMovingAverage'>
            }
        }),
        ('weights', {
            'MurreyMathSignals': 1.0,
            'HullMovingAverage': 1.0
        })
    )
