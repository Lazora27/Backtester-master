import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ParabolicTimePrice_SymmetricalTriangle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ParabolicTimePrice und SymmetricalTriangle
    """
    
    params = (
        ('indicators', {
            'ParabolicTimePrice': {
                'class': ParabolicTimePrice,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ParabolicTimePrice'>
            },
            'SymmetricalTriangle': {
                'class': SymmetricalTriangle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SymmetricalTriangle'>
            }
        }),
        ('weights', {
            'ParabolicTimePrice': 1.0,
            'SymmetricalTriangle': 1.0
        })
    )
