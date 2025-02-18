import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BalanceMomentum_OpenInterest_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BalanceMomentum und OpenInterest
    """
    
    params = (
        ('indicators', {
            'BalanceMomentum': {
                'class': BalanceMomentum,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BalanceMomentum'>
            },
            'OpenInterest': {
                'class': OpenInterest,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OpenInterest'>
            }
        }),
        ('weights', {
            'BalanceMomentum': 1.0,
            'OpenInterest': 1.0
        })
    )
