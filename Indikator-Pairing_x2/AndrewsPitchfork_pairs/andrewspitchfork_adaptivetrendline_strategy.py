import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AndrewsPitchfork_AdaptiveTrendLine_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AndrewsPitchfork und AdaptiveTrendLine
    """
    
    params = (
        ('indicators', {
            'AndrewsPitchfork': {
                'class': AndrewsPitchfork,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AndrewsPitchfork'>
            },
            'AdaptiveTrendLine': {
                'class': AdaptiveTrendLine,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveTrendLine'>
            }
        }),
        ('weights', {
            'AndrewsPitchfork': 1.0,
            'AdaptiveTrendLine': 1.0
        })
    )
