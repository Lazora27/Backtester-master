import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BalanceMomentum_SymmetricalTriangle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BalanceMomentum und SymmetricalTriangle
    """
    
    params = (
        ('indicators', {
            'BalanceMomentum': {
                'class': BalanceMomentum,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BalanceMomentum'>
            },
            'SymmetricalTriangle': {
                'class': SymmetricalTriangle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SymmetricalTriangle'>
            }
        }),
        ('weights', {
            'BalanceMomentum': 1.0,
            'SymmetricalTriangle': 1.0
        })
    )
