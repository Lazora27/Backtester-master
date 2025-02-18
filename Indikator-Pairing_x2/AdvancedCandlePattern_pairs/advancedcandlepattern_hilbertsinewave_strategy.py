import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AdvancedCandlePattern_HilbertSinewave_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AdvancedCandlePattern und HilbertSinewave
    """
    
    params = (
        ('indicators', {
            'AdvancedCandlePattern': {
                'class': AdvancedCandlePattern,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdvancedCandlePattern'>
            },
            'HilbertSinewave': {
                'class': HilbertSinewave,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertSinewave'>
            }
        }),
        ('weights', {
            'AdvancedCandlePattern': 1.0,
            'HilbertSinewave': 1.0
        })
    )
