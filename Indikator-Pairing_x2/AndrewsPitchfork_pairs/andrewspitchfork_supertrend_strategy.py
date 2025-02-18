import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AndrewsPitchfork_SuperTrend_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AndrewsPitchfork und SuperTrend
    """
    
    params = (
        ('indicators', {
            'AndrewsPitchfork': {
                'class': AndrewsPitchfork,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AndrewsPitchfork'>
            },
            'SuperTrend': {
                'class': SuperTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SuperTrend'>
            }
        }),
        ('weights', {
            'AndrewsPitchfork': 1.0,
            'SuperTrend': 1.0
        })
    )
