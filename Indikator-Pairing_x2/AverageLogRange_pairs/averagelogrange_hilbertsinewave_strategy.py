import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AverageLogRange_HilbertSinewave_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AverageLogRange und HilbertSinewave
    """
    
    params = (
        ('indicators', {
            'AverageLogRange': {
                'class': AverageLogRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageLogRange'>
            },
            'HilbertSinewave': {
                'class': HilbertSinewave,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertSinewave'>
            }
        }),
        ('weights', {
            'AverageLogRange': 1.0,
            'HilbertSinewave': 1.0
        })
    )
