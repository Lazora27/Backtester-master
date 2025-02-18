import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TrueRange_HilbertSinewave_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TrueRange und HilbertSinewave
    """
    
    params = (
        ('indicators', {
            'TrueRange': {
                'class': TrueRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrueRange1'>
            },
            'HilbertSinewave': {
                'class': HilbertSinewave,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertSinewave'>
            }
        }),
        ('weights', {
            'TrueRange': 1.0,
            'HilbertSinewave': 1.0
        })
    )
