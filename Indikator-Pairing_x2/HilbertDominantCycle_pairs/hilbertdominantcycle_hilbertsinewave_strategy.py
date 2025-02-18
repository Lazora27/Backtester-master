import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HilbertDominantCycle_HilbertSinewave_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HilbertDominantCycle und HilbertSinewave
    """
    
    params = (
        ('indicators', {
            'HilbertDominantCycle': {
                'class': HilbertDominantCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertDominantCycle'>
            },
            'HilbertSinewave': {
                'class': HilbertSinewave,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertSinewave'>
            }
        }),
        ('weights', {
            'HilbertDominantCycle': 1.0,
            'HilbertSinewave': 1.0
        })
    )
