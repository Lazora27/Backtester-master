import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticRSI_HilbertSinewave_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticRSI und HilbertSinewave
    """
    
    params = (
        ('indicators', {
            'StochasticRSI': {
                'class': StochasticRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticRSI'>
            },
            'HilbertSinewave': {
                'class': HilbertSinewave,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertSinewave'>
            }
        }),
        ('weights', {
            'StochasticRSI': 1.0,
            'HilbertSinewave': 1.0
        })
    )
