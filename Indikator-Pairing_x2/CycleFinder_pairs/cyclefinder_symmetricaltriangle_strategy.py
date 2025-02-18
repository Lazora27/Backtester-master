import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CycleFinder_SymmetricalTriangle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CycleFinder und SymmetricalTriangle
    """
    
    params = (
        ('indicators', {
            'CycleFinder': {
                'class': CycleFinder,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CycleFinder'>
            },
            'SymmetricalTriangle': {
                'class': SymmetricalTriangle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SymmetricalTriangle'>
            }
        }),
        ('weights', {
            'CycleFinder': 1.0,
            'SymmetricalTriangle': 1.0
        })
    )
