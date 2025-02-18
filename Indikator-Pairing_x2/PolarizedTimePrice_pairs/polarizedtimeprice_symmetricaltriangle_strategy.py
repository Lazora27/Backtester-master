import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PolarizedTimePrice_SymmetricalTriangle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PolarizedTimePrice und SymmetricalTriangle
    """
    
    params = (
        ('indicators', {
            'PolarizedTimePrice': {
                'class': PolarizedTimePrice,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PolarizedTimePrice'>
            },
            'SymmetricalTriangle': {
                'class': SymmetricalTriangle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SymmetricalTriangle'>
            }
        }),
        ('weights', {
            'PolarizedTimePrice': 1.0,
            'SymmetricalTriangle': 1.0
        })
    )
