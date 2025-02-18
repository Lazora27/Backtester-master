import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BalanceMomentum_PhaseDivergence_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BalanceMomentum und PhaseDivergence
    """
    
    params = (
        ('indicators', {
            'BalanceMomentum': {
                'class': BalanceMomentum,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BalanceMomentum'>
            },
            'PhaseDivergence': {
                'class': PhaseDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PhaseDivergence'>
            }
        }),
        ('weights', {
            'BalanceMomentum': 1.0,
            'PhaseDivergence': 1.0
        })
    )
