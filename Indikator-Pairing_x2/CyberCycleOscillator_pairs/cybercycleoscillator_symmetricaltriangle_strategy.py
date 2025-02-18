import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CyberCycleOscillator_SymmetricalTriangle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CyberCycleOscillator und SymmetricalTriangle
    """
    
    params = (
        ('indicators', {
            'CyberCycleOscillator': {
                'class': CyberCycleOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CyberCycleOscillator'>
            },
            'SymmetricalTriangle': {
                'class': SymmetricalTriangle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SymmetricalTriangle'>
            }
        }),
        ('weights', {
            'CyberCycleOscillator': 1.0,
            'SymmetricalTriangle': 1.0
        })
    )
