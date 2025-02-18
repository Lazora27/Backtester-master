import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ChoppinessIndex_HilbertSinewave_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ChoppinessIndex und HilbertSinewave
    """
    
    params = (
        ('indicators', {
            'ChoppinessIndex': {
                'class': ChoppinessIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChoppinessIndex'>
            },
            'HilbertSinewave': {
                'class': HilbertSinewave,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertSinewave'>
            }
        }),
        ('weights', {
            'ChoppinessIndex': 1.0,
            'HilbertSinewave': 1.0
        })
    )
