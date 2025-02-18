import backtrader as bt
from ..base_strategy import FlexibleStrategy

class McClellanOscillator_SymmetricalTriangle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von McClellanOscillator und SymmetricalTriangle
    """
    
    params = (
        ('indicators', {
            'McClellanOscillator': {
                'class': McClellanOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_McClellanOscillator'>
            },
            'SymmetricalTriangle': {
                'class': SymmetricalTriangle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SymmetricalTriangle'>
            }
        }),
        ('weights', {
            'McClellanOscillator': 1.0,
            'SymmetricalTriangle': 1.0
        })
    )
