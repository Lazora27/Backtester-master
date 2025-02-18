import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AdaptiveRSI_AndrewsPitchfork_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AdaptiveRSI und AndrewsPitchfork
    """
    
    params = (
        ('indicators', {
            'AdaptiveRSI': {
                'class': AdaptiveRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveRSI'>
            },
            'AndrewsPitchfork': {
                'class': AndrewsPitchfork,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AndrewsPitchfork'>
            }
        }),
        ('weights', {
            'AdaptiveRSI': 1.0,
            'AndrewsPitchfork': 1.0
        })
    )
