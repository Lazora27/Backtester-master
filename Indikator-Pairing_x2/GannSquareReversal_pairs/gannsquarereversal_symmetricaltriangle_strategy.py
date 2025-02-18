import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannSquareReversal_SymmetricalTriangle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannSquareReversal und SymmetricalTriangle
    """
    
    params = (
        ('indicators', {
            'GannSquareReversal': {
                'class': GannSquareReversal,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannSquareReversal'>
            },
            'SymmetricalTriangle': {
                'class': SymmetricalTriangle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SymmetricalTriangle'>
            }
        }),
        ('weights', {
            'GannSquareReversal': 1.0,
            'SymmetricalTriangle': 1.0
        })
    )
