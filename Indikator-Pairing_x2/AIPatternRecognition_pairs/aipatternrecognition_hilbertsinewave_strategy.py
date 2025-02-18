import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AIPatternRecognition_HilbertSinewave_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AIPatternRecognition und HilbertSinewave
    """
    
    params = (
        ('indicators', {
            'AIPatternRecognition': {
                'class': AIPatternRecognition,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AIPatternRecognition'>
            },
            'HilbertSinewave': {
                'class': HilbertSinewave,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertSinewave'>
            }
        }),
        ('weights', {
            'AIPatternRecognition': 1.0,
            'HilbertSinewave': 1.0
        })
    )
