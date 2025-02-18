import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AndrewsPitchfork_RandomWalkIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AndrewsPitchfork und RandomWalkIndex
    """
    
    params = (
        ('indicators', {
            'AndrewsPitchfork': {
                'class': AndrewsPitchfork,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AndrewsPitchfork'>
            },
            'RandomWalkIndex': {
                'class': RandomWalkIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RandomWalkIndex'>
            }
        }),
        ('weights', {
            'AndrewsPitchfork': 1.0,
            'RandomWalkIndex': 1.0
        })
    )
