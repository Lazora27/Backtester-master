import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannSquares_HilbertSinewave_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannSquares und HilbertSinewave
    """
    
    params = (
        ('indicators', {
            'GannSquares': {
                'class': GannSquares,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannSquares'>
            },
            'HilbertSinewave': {
                'class': HilbertSinewave,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertSinewave'>
            }
        }),
        ('weights', {
            'GannSquares': 1.0,
            'HilbertSinewave': 1.0
        })
    )
