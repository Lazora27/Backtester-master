import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AndrewsPitchfork_EaseOfMovement_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AndrewsPitchfork und EaseOfMovement
    """
    
    params = (
        ('indicators', {
            'AndrewsPitchfork': {
                'class': AndrewsPitchfork,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AndrewsPitchfork'>
            },
            'EaseOfMovement': {
                'class': EaseOfMovement,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EaseOfMovement1'>
            }
        }),
        ('weights', {
            'AndrewsPitchfork': 1.0,
            'EaseOfMovement': 1.0
        })
    )
