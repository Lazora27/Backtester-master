import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ExtensionProjections_SymmetricalTriangle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ExtensionProjections und SymmetricalTriangle
    """
    
    params = (
        ('indicators', {
            'ExtensionProjections': {
                'class': ExtensionProjections,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ExtensionProjections'>
            },
            'SymmetricalTriangle': {
                'class': SymmetricalTriangle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SymmetricalTriangle'>
            }
        }),
        ('weights', {
            'ExtensionProjections': 1.0,
            'SymmetricalTriangle': 1.0
        })
    )
