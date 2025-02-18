import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AndrewsPitchfork_GannSquares_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AndrewsPitchfork und GannSquares
    """
    
    params = (
        ('indicators', {
            'AndrewsPitchfork': {
                'class': AndrewsPitchfork,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AndrewsPitchfork'>
            },
            'GannSquares': {
                'class': GannSquares,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannSquares'>
            }
        }),
        ('weights', {
            'AndrewsPitchfork': 1.0,
            'GannSquares': 1.0
        })
    )
