import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FractalAdaptiveCycle_HilbertSinewave_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FractalAdaptiveCycle und HilbertSinewave
    """
    
    params = (
        ('indicators', {
            'FractalAdaptiveCycle': {
                'class': FractalAdaptiveCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FractalAdaptiveCycle'>
            },
            'HilbertSinewave': {
                'class': HilbertSinewave,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertSinewave'>
            }
        }),
        ('weights', {
            'FractalAdaptiveCycle': 1.0,
            'HilbertSinewave': 1.0
        })
    )
