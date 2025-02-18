import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticDivergence_HilbertSinewave_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticDivergence und HilbertSinewave
    """
    
    params = (
        ('indicators', {
            'StochasticDivergence': {
                'class': StochasticDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticDivergence'>
            },
            'HilbertSinewave': {
                'class': HilbertSinewave,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertSinewave'>
            }
        }),
        ('weights', {
            'StochasticDivergence': 1.0,
            'HilbertSinewave': 1.0
        })
    )
