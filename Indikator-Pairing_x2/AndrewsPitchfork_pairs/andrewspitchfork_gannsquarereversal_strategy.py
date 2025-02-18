import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AndrewsPitchfork_GannSquareReversal_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AndrewsPitchfork und GannSquareReversal
    """
    
    params = (
        ('indicators', {
            'AndrewsPitchfork': {
                'class': AndrewsPitchfork,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AndrewsPitchfork'>
            },
            'GannSquareReversal': {
                'class': GannSquareReversal,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannSquareReversal'>
            }
        }),
        ('weights', {
            'AndrewsPitchfork': 1.0,
            'GannSquareReversal': 1.0
        })
    )
