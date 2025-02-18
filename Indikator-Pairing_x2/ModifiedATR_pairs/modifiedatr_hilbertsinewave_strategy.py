import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ModifiedATR_HilbertSinewave_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ModifiedATR und HilbertSinewave
    """
    
    params = (
        ('indicators', {
            'ModifiedATR': {
                'class': ModifiedATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ModifiedATR'>
            },
            'HilbertSinewave': {
                'class': HilbertSinewave,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertSinewave'>
            }
        }),
        ('weights', {
            'ModifiedATR': 1.0,
            'HilbertSinewave': 1.0
        })
    )
