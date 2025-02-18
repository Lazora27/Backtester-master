import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ModifiedATR_SymmetricalTriangle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ModifiedATR und SymmetricalTriangle
    """
    
    params = (
        ('indicators', {
            'ModifiedATR': {
                'class': ModifiedATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ModifiedATR'>
            },
            'SymmetricalTriangle': {
                'class': SymmetricalTriangle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SymmetricalTriangle'>
            }
        }),
        ('weights', {
            'ModifiedATR': 1.0,
            'SymmetricalTriangle': 1.0
        })
    )
