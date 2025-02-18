import backtrader as bt
from ..base_strategy import FlexibleStrategy

class Fisher_AndrewsPitchfork_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von Fisher und AndrewsPitchfork
    """
    
    params = (
        ('indicators', {
            'Fisher': {
                'class': Fisher,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_Fisher'>
            },
            'AndrewsPitchfork': {
                'class': AndrewsPitchfork,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AndrewsPitchfork'>
            }
        }),
        ('weights', {
            'Fisher': 1.0,
            'AndrewsPitchfork': 1.0
        })
    )
