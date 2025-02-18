import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SymmetricalTriangle_WeightedCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SymmetricalTriangle und WeightedCycle
    """
    
    params = (
        ('indicators', {
            'SymmetricalTriangle': {
                'class': SymmetricalTriangle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SymmetricalTriangle'>
            },
            'WeightedCycle': {
                'class': WeightedCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeightedCycle'>
            }
        }),
        ('weights', {
            'SymmetricalTriangle': 1.0,
            'WeightedCycle': 1.0
        })
    )
