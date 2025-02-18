import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RSIDivergence_HilbertSinewave_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RSIDivergence und HilbertSinewave
    """
    
    params = (
        ('indicators', {
            'RSIDivergence': {
                'class': RSIDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RSIDivergence'>
            },
            'HilbertSinewave': {
                'class': HilbertSinewave,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertSinewave'>
            }
        }),
        ('weights', {
            'RSIDivergence': 1.0,
            'HilbertSinewave': 1.0
        })
    )
