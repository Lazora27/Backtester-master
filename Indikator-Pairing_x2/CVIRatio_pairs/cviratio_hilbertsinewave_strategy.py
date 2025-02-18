import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CVIRatio_HilbertSinewave_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CVIRatio und HilbertSinewave
    """
    
    params = (
        ('indicators', {
            'CVIRatio': {
                'class': CVIRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CVIRatio'>
            },
            'HilbertSinewave': {
                'class': HilbertSinewave,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertSinewave'>
            }
        }),
        ('weights', {
            'CVIRatio': 1.0,
            'HilbertSinewave': 1.0
        })
    )
