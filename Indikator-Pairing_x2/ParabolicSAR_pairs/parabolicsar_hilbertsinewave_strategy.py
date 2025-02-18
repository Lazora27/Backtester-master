import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ParabolicSAR_HilbertSinewave_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ParabolicSAR und HilbertSinewave
    """
    
    params = (
        ('indicators', {
            'ParabolicSAR': {
                'class': ParabolicSAR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ParabolicSAR'>
            },
            'HilbertSinewave': {
                'class': HilbertSinewave,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertSinewave'>
            }
        }),
        ('weights', {
            'ParabolicSAR': 1.0,
            'HilbertSinewave': 1.0
        })
    )
