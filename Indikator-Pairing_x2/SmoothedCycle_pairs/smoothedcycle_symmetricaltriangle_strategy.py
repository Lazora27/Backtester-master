import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SmoothedCycle_SymmetricalTriangle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SmoothedCycle und SymmetricalTriangle
    """
    
    params = (
        ('indicators', {
            'SmoothedCycle': {
                'class': SmoothedCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmoothedCycle'>
            },
            'SymmetricalTriangle': {
                'class': SymmetricalTriangle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SymmetricalTriangle'>
            }
        }),
        ('weights', {
            'SmoothedCycle': 1.0,
            'SymmetricalTriangle': 1.0
        })
    )
