import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AndrewsPitchfork_PivotPoints_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AndrewsPitchfork und PivotPoints
    """
    
    params = (
        ('indicators', {
            'AndrewsPitchfork': {
                'class': AndrewsPitchfork,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AndrewsPitchfork'>
            },
            'PivotPoints': {
                'class': PivotPoints,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PivotPoints'>
            }
        }),
        ('weights', {
            'AndrewsPitchfork': 1.0,
            'PivotPoints': 1.0
        })
    )
