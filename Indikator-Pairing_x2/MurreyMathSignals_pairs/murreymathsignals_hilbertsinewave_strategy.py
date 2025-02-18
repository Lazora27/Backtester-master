import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MurreyMathSignals_HilbertSinewave_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MurreyMathSignals und HilbertSinewave
    """
    
    params = (
        ('indicators', {
            'MurreyMathSignals': {
                'class': MurreyMathSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MurreyMathSignals'>
            },
            'HilbertSinewave': {
                'class': HilbertSinewave,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertSinewave'>
            }
        }),
        ('weights', {
            'MurreyMathSignals': 1.0,
            'HilbertSinewave': 1.0
        })
    )
