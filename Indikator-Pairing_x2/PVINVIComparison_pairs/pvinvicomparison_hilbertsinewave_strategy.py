import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PVINVIComparison_HilbertSinewave_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PVINVIComparison und HilbertSinewave
    """
    
    params = (
        ('indicators', {
            'PVINVIComparison': {
                'class': PVINVIComparison,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PVINVIComparison'>
            },
            'HilbertSinewave': {
                'class': HilbertSinewave,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertSinewave'>
            }
        }),
        ('weights', {
            'PVINVIComparison': 1.0,
            'HilbertSinewave': 1.0
        })
    )
