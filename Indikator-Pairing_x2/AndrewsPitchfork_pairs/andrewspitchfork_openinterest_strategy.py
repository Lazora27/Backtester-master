import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AndrewsPitchfork_OpenInterest_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AndrewsPitchfork und OpenInterest
    """
    
    params = (
        ('indicators', {
            'AndrewsPitchfork': {
                'class': AndrewsPitchfork,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AndrewsPitchfork'>
            },
            'OpenInterest': {
                'class': OpenInterest,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OpenInterest'>
            }
        }),
        ('weights', {
            'AndrewsPitchfork': 1.0,
            'OpenInterest': 1.0
        })
    )
