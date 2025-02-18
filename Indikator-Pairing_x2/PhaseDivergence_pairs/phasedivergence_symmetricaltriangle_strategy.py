import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PhaseDivergence_SymmetricalTriangle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PhaseDivergence und SymmetricalTriangle
    """
    
    params = (
        ('indicators', {
            'PhaseDivergence': {
                'class': PhaseDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PhaseDivergence'>
            },
            'SymmetricalTriangle': {
                'class': SymmetricalTriangle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SymmetricalTriangle'>
            }
        }),
        ('weights', {
            'PhaseDivergence': 1.0,
            'SymmetricalTriangle': 1.0
        })
    )
