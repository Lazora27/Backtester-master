import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SymmetricalTriangle_WeeklyCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SymmetricalTriangle und WeeklyCycle
    """
    
    params = (
        ('indicators', {
            'SymmetricalTriangle': {
                'class': SymmetricalTriangle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SymmetricalTriangle'>
            },
            'WeeklyCycle': {
                'class': WeeklyCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeeklyCycle'>
            }
        }),
        ('weights', {
            'SymmetricalTriangle': 1.0,
            'WeeklyCycle': 1.0
        })
    )
