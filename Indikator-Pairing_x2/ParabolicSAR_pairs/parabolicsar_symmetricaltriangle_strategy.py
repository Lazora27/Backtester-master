import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ParabolicSAR_SymmetricalTriangle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ParabolicSAR und SymmetricalTriangle
    """
    
    params = (
        ('indicators', {
            'ParabolicSAR': {
                'class': ParabolicSAR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ParabolicSAR'>
            },
            'SymmetricalTriangle': {
                'class': SymmetricalTriangle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SymmetricalTriangle'>
            }
        }),
        ('weights', {
            'ParabolicSAR': 1.0,
            'SymmetricalTriangle': 1.0
        })
    )
