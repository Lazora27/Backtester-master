import backtrader as bt
from ..base_strategy import FlexibleStrategy

class Fisher_SymmetricalTriangle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von Fisher und SymmetricalTriangle
    """
    
    params = (
        ('indicators', {
            'Fisher': {
                'class': Fisher,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_Fisher'>
            },
            'SymmetricalTriangle': {
                'class': SymmetricalTriangle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SymmetricalTriangle'>
            }
        }),
        ('weights', {
            'Fisher': 1.0,
            'SymmetricalTriangle': 1.0
        })
    )
