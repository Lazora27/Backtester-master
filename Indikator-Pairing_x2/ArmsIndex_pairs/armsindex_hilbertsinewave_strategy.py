import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ArmsIndex_HilbertSinewave_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ArmsIndex und HilbertSinewave
    """
    
    params = (
        ('indicators', {
            'ArmsIndex': {
                'class': ArmsIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ArmsIndex'>
            },
            'HilbertSinewave': {
                'class': HilbertSinewave,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertSinewave'>
            }
        }),
        ('weights', {
            'ArmsIndex': 1.0,
            'HilbertSinewave': 1.0
        })
    )
