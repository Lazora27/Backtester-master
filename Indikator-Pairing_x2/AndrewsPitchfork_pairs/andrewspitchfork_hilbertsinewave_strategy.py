import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AndrewsPitchfork_HilbertSinewave_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AndrewsPitchfork und HilbertSinewave
    """
    
    params = (
        ('indicators', {
            'AndrewsPitchfork': {
                'class': AndrewsPitchfork,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AndrewsPitchfork'>
            },
            'HilbertSinewave': {
                'class': HilbertSinewave,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertSinewave'>
            }
        }),
        ('weights', {
            'AndrewsPitchfork': 1.0,
            'HilbertSinewave': 1.0
        })
    )
