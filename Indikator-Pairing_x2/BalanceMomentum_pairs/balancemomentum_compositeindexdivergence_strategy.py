import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BalanceMomentum_CompositeIndexDivergence_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BalanceMomentum und CompositeIndexDivergence
    """
    
    params = (
        ('indicators', {
            'BalanceMomentum': {
                'class': BalanceMomentum,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BalanceMomentum'>
            },
            'CompositeIndexDivergence': {
                'class': CompositeIndexDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CompositeIndexDivergence'>
            }
        }),
        ('weights', {
            'BalanceMomentum': 1.0,
            'CompositeIndexDivergence': 1.0
        })
    )
