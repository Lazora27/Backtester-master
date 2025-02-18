import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AutoFibonacci_SymmetricalTriangle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AutoFibonacci und SymmetricalTriangle
    """
    
    params = (
        ('indicators', {
            'AutoFibonacci': {
                'class': AutoFibonacci,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AutoFibonacci'>
            },
            'SymmetricalTriangle': {
                'class': SymmetricalTriangle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SymmetricalTriangle'>
            }
        }),
        ('weights', {
            'AutoFibonacci': 1.0,
            'SymmetricalTriangle': 1.0
        })
    )
