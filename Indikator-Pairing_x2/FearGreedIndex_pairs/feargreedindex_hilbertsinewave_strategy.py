import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FearGreedIndex_HilbertSinewave_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FearGreedIndex und HilbertSinewave
    """
    
    params = (
        ('indicators', {
            'FearGreedIndex': {
                'class': FearGreedIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FearGreedIndex'>
            },
            'HilbertSinewave': {
                'class': HilbertSinewave,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertSinewave'>
            }
        }),
        ('weights', {
            'FearGreedIndex': 1.0,
            'HilbertSinewave': 1.0
        })
    )
