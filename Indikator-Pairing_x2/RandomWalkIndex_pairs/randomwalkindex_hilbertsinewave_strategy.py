import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RandomWalkIndex_HilbertSinewave_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RandomWalkIndex und HilbertSinewave
    """
    
    params = (
        ('indicators', {
            'RandomWalkIndex': {
                'class': RandomWalkIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RandomWalkIndex'>
            },
            'HilbertSinewave': {
                'class': HilbertSinewave,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertSinewave'>
            }
        }),
        ('weights', {
            'RandomWalkIndex': 1.0,
            'HilbertSinewave': 1.0
        })
    )
