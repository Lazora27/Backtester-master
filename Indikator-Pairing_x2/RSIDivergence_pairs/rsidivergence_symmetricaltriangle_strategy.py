import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RSIDivergence_SymmetricalTriangle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RSIDivergence und SymmetricalTriangle
    """
    
    params = (
        ('indicators', {
            'RSIDivergence': {
                'class': RSIDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RSIDivergence'>
            },
            'SymmetricalTriangle': {
                'class': SymmetricalTriangle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SymmetricalTriangle'>
            }
        }),
        ('weights', {
            'RSIDivergence': 1.0,
            'SymmetricalTriangle': 1.0
        })
    )
