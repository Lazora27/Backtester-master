import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AdvanceDeclineLine_HilbertSinewave_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AdvanceDeclineLine und HilbertSinewave
    """
    
    params = (
        ('indicators', {
            'AdvanceDeclineLine': {
                'class': AdvanceDeclineLine,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdvanceDeclineLine'>
            },
            'HilbertSinewave': {
                'class': HilbertSinewave,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertSinewave'>
            }
        }),
        ('weights', {
            'AdvanceDeclineLine': 1.0,
            'HilbertSinewave': 1.0
        })
    )
