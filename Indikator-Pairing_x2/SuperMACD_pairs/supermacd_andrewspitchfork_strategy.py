import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SuperMACD_AndrewsPitchfork_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SuperMACD und AndrewsPitchfork
    """
    
    params = (
        ('indicators', {
            'SuperMACD': {
                'class': SuperMACD,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SuperMACD'>
            },
            'AndrewsPitchfork': {
                'class': AndrewsPitchfork,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AndrewsPitchfork'>
            }
        }),
        ('weights', {
            'SuperMACD': 1.0,
            'AndrewsPitchfork': 1.0
        })
    )
