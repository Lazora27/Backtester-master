import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BalanceMomentum_ChoppinessIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BalanceMomentum und ChoppinessIndex
    """
    
    params = (
        ('indicators', {
            'BalanceMomentum': {
                'class': BalanceMomentum,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BalanceMomentum'>
            },
            'ChoppinessIndex': {
                'class': ChoppinessIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChoppinessIndex'>
            }
        }),
        ('weights', {
            'BalanceMomentum': 1.0,
            'ChoppinessIndex': 1.0
        })
    )
