import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannSquares_SymmetricalTriangle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannSquares und SymmetricalTriangle
    """
    
    params = (
        ('indicators', {
            'GannSquares': {
                'class': GannSquares,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannSquares'>
            },
            'SymmetricalTriangle': {
                'class': SymmetricalTriangle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SymmetricalTriangle'>
            }
        }),
        ('weights', {
            'GannSquares': 1.0,
            'SymmetricalTriangle': 1.0
        })
    )
