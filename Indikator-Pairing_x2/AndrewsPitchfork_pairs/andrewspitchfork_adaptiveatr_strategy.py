import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AndrewsPitchfork_AdaptiveATR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AndrewsPitchfork und AdaptiveATR
    """
    
    params = (
        ('indicators', {
            'AndrewsPitchfork': {
                'class': AndrewsPitchfork,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AndrewsPitchfork'>
            },
            'AdaptiveATR': {
                'class': AdaptiveATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveATR'>
            }
        }),
        ('weights', {
            'AndrewsPitchfork': 1.0,
            'AdaptiveATR': 1.0
        })
    )
