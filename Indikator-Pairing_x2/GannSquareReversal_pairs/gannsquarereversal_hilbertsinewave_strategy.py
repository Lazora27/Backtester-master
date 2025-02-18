import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannSquareReversal_HilbertSinewave_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannSquareReversal und HilbertSinewave
    """
    
    params = (
        ('indicators', {
            'GannSquareReversal': {
                'class': GannSquareReversal,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannSquareReversal'>
            },
            'HilbertSinewave': {
                'class': HilbertSinewave,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertSinewave'>
            }
        }),
        ('weights', {
            'GannSquareReversal': 1.0,
            'HilbertSinewave': 1.0
        })
    )
