import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SuperMACD_SymmetricalTriangle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SuperMACD und SymmetricalTriangle
    """
    
    params = (
        ('indicators', {
            'SuperMACD': {
                'class': SuperMACD,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SuperMACD'>
            },
            'SymmetricalTriangle': {
                'class': SymmetricalTriangle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SymmetricalTriangle'>
            }
        }),
        ('weights', {
            'SuperMACD': 1.0,
            'SymmetricalTriangle': 1.0
        })
    )
