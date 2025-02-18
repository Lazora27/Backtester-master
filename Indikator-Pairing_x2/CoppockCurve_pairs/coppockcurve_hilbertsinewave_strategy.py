import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CoppockCurve_HilbertSinewave_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CoppockCurve und HilbertSinewave
    """
    
    params = (
        ('indicators', {
            'CoppockCurve': {
                'class': CoppockCurve,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CoppockCurve'>
            },
            'HilbertSinewave': {
                'class': HilbertSinewave,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertSinewave'>
            }
        }),
        ('weights', {
            'CoppockCurve': 1.0,
            'HilbertSinewave': 1.0
        })
    )
