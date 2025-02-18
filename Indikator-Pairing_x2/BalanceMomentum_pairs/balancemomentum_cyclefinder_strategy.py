import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BalanceMomentum_CycleFinder_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BalanceMomentum und CycleFinder
    """
    
    params = (
        ('indicators', {
            'BalanceMomentum': {
                'class': BalanceMomentum,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BalanceMomentum'>
            },
            'CycleFinder': {
                'class': CycleFinder,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CycleFinder'>
            }
        }),
        ('weights', {
            'BalanceMomentum': 1.0,
            'CycleFinder': 1.0
        })
    )
