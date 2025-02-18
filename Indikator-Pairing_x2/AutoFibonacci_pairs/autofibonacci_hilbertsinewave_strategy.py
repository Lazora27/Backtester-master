import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AutoFibonacci_HilbertSinewave_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AutoFibonacci und HilbertSinewave
    """
    
    params = (
        ('indicators', {
            'AutoFibonacci': {
                'class': AutoFibonacci,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AutoFibonacci'>
            },
            'HilbertSinewave': {
                'class': HilbertSinewave,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertSinewave'>
            }
        }),
        ('weights', {
            'AutoFibonacci': 1.0,
            'HilbertSinewave': 1.0
        })
    )
