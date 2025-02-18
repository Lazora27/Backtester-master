import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AndrewsPitchfork_ChoppinessIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AndrewsPitchfork und ChoppinessIndex
    """
    
    params = (
        ('indicators', {
            'AndrewsPitchfork': {
                'class': AndrewsPitchfork,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AndrewsPitchfork'>
            },
            'ChoppinessIndex': {
                'class': ChoppinessIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChoppinessIndex'>
            }
        }),
        ('weights', {
            'AndrewsPitchfork': 1.0,
            'ChoppinessIndex': 1.0
        })
    )
