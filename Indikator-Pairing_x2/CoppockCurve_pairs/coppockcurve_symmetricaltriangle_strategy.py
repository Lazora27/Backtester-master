import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CoppockCurve_SymmetricalTriangle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CoppockCurve und SymmetricalTriangle
    """
    
    params = (
        ('indicators', {
            'CoppockCurve': {
                'class': CoppockCurve,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CoppockCurve'>
            },
            'SymmetricalTriangle': {
                'class': SymmetricalTriangle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SymmetricalTriangle'>
            }
        }),
        ('weights', {
            'CoppockCurve': 1.0,
            'SymmetricalTriangle': 1.0
        })
    )
