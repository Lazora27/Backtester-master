import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PhaseDivergence_HilbertSinewave_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PhaseDivergence und HilbertSinewave
    """
    
    params = (
        ('indicators', {
            'PhaseDivergence': {
                'class': PhaseDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PhaseDivergence'>
            },
            'HilbertSinewave': {
                'class': HilbertSinewave,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertSinewave'>
            }
        }),
        ('weights', {
            'PhaseDivergence': 1.0,
            'HilbertSinewave': 1.0
        })
    )
