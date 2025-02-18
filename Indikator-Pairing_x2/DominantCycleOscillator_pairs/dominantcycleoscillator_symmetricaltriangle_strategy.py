import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DominantCycleOscillator_SymmetricalTriangle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DominantCycleOscillator und SymmetricalTriangle
    """
    
    params = (
        ('indicators', {
            'DominantCycleOscillator': {
                'class': DominantCycleOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DominantCycleOscillator'>
            },
            'SymmetricalTriangle': {
                'class': SymmetricalTriangle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SymmetricalTriangle'>
            }
        }),
        ('weights', {
            'DominantCycleOscillator': 1.0,
            'SymmetricalTriangle': 1.0
        })
    )
