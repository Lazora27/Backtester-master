import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticDivergence_SymmetricalTriangle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticDivergence und SymmetricalTriangle
    """
    
    params = (
        ('indicators', {
            'StochasticDivergence': {
                'class': StochasticDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticDivergence'>
            },
            'SymmetricalTriangle': {
                'class': SymmetricalTriangle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SymmetricalTriangle'>
            }
        }),
        ('weights', {
            'StochasticDivergence': 1.0,
            'SymmetricalTriangle': 1.0
        })
    )
