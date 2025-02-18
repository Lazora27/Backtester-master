import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SymmetricalTriangle_TimeCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SymmetricalTriangle und TimeCycle
    """
    
    params = (
        ('indicators', {
            'SymmetricalTriangle': {
                'class': SymmetricalTriangle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SymmetricalTriangle'>
            },
            'TimeCycle': {
                'class': TimeCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeCycle'>
            }
        }),
        ('weights', {
            'SymmetricalTriangle': 1.0,
            'TimeCycle': 1.0
        })
    )
