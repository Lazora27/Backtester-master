import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AdvanceDeclineLine_BalanceMomentum_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AdvanceDeclineLine und BalanceMomentum
    """
    
    params = (
        ('indicators', {
            'AdvanceDeclineLine': {
                'class': AdvanceDeclineLine,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdvanceDeclineLine'>
            },
            'BalanceMomentum': {
                'class': BalanceMomentum,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BalanceMomentum'>
            }
        }),
        ('weights', {
            'AdvanceDeclineLine': 1.0,
            'BalanceMomentum': 1.0
        })
    )
