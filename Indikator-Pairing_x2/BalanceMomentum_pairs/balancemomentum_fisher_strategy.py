import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BalanceMomentum_Fisher_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BalanceMomentum und Fisher
    """
    
    params = (
        ('indicators', {
            'BalanceMomentum': {
                'class': BalanceMomentum,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BalanceMomentum'>
            },
            'Fisher': {
                'class': Fisher,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_Fisher'>
            }
        }),
        ('weights', {
            'BalanceMomentum': 1.0,
            'Fisher': 1.0
        })
    )
