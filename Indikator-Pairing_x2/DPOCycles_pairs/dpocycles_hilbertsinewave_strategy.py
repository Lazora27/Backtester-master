import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DPOCycles_HilbertSinewave_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DPOCycles und HilbertSinewave
    """
    
    params = (
        ('indicators', {
            'DPOCycles': {
                'class': DPOCycles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DPOCycles'>
            },
            'HilbertSinewave': {
                'class': HilbertSinewave,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertSinewave'>
            }
        }),
        ('weights', {
            'DPOCycles': 1.0,
            'HilbertSinewave': 1.0
        })
    )
