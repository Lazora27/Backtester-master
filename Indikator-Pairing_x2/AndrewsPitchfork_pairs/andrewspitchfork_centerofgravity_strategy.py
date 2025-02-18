import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AndrewsPitchfork_CenterOfGravity_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AndrewsPitchfork und CenterOfGravity
    """
    
    params = (
        ('indicators', {
            'AndrewsPitchfork': {
                'class': AndrewsPitchfork,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AndrewsPitchfork'>
            },
            'CenterOfGravity': {
                'class': CenterOfGravity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CenterOfGravity'>
            }
        }),
        ('weights', {
            'AndrewsPitchfork': 1.0,
            'CenterOfGravity': 1.0
        })
    )
