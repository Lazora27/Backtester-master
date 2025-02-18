import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WolfeWaves_HilbertSinewave_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WolfeWaves und HilbertSinewave
    """
    
    params = (
        ('indicators', {
            'WolfeWaves': {
                'class': WolfeWaves,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WolfeWaves'>
            },
            'HilbertSinewave': {
                'class': HilbertSinewave,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertSinewave'>
            }
        }),
        ('weights', {
            'WolfeWaves': 1.0,
            'HilbertSinewave': 1.0
        })
    )
