import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RSIDivergence_BalanceMomentum_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RSIDivergence und BalanceMomentum
    """
    
    params = (
        ('indicators', {
            'RSIDivergence': {
                'class': RSIDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RSIDivergence'>
            },
            'BalanceMomentum': {
                'class': BalanceMomentum,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BalanceMomentum'>
            }
        }),
        ('weights', {
            'RSIDivergence': 1.0,
            'BalanceMomentum': 1.0
        })
    )
