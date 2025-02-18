import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BarStrength_SymmetricalTriangle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BarStrength und SymmetricalTriangle
    """
    
    params = (
        ('indicators', {
            'BarStrength': {
                'class': BarStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BarStrength'>
            },
            'SymmetricalTriangle': {
                'class': SymmetricalTriangle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SymmetricalTriangle'>
            }
        }),
        ('weights', {
            'BarStrength': 1.0,
            'SymmetricalTriangle': 1.0
        })
    )
