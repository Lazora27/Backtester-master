import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BalanceMomentum_MassIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BalanceMomentum und MassIndex
    """
    
    params = (
        ('indicators', {
            'BalanceMomentum': {
                'class': BalanceMomentum,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BalanceMomentum'>
            },
            'MassIndex': {
                'class': MassIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MassIndex'>
            }
        }),
        ('weights', {
            'BalanceMomentum': 1.0,
            'MassIndex': 1.0
        })
    )
