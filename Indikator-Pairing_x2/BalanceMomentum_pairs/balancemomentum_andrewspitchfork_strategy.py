import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BalanceMomentum_AndrewsPitchfork_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BalanceMomentum und AndrewsPitchfork
    """
    
    params = (
        ('indicators', {
            'BalanceMomentum': {
                'class': BalanceMomentum,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BalanceMomentum'>
            },
            'AndrewsPitchfork': {
                'class': AndrewsPitchfork,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AndrewsPitchfork'>
            }
        }),
        ('weights', {
            'BalanceMomentum': 1.0,
            'AndrewsPitchfork': 1.0
        })
    )
