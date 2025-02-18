import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VWAPBands_HilbertSinewave_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VWAPBands und HilbertSinewave
    """
    
    params = (
        ('indicators', {
            'VWAPBands': {
                'class': VWAPBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VWAPBands'>
            },
            'HilbertSinewave': {
                'class': HilbertSinewave,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertSinewave'>
            }
        }),
        ('weights', {
            'VWAPBands': 1.0,
            'HilbertSinewave': 1.0
        })
    )
