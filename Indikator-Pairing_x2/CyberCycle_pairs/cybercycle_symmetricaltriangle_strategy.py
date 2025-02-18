import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CyberCycle_SymmetricalTriangle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CyberCycle und SymmetricalTriangle
    """
    
    params = (
        ('indicators', {
            'CyberCycle': {
                'class': CyberCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CyberCycle'>
            },
            'SymmetricalTriangle': {
                'class': SymmetricalTriangle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SymmetricalTriangle'>
            }
        }),
        ('weights', {
            'CyberCycle': 1.0,
            'SymmetricalTriangle': 1.0
        })
    )
