import backtrader as bt
from ..base_strategy import FlexibleStrategy

class EaseOfMovement_SymmetricalTriangle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von EaseOfMovement und SymmetricalTriangle
    """
    
    params = (
        ('indicators', {
            'EaseOfMovement': {
                'class': EaseOfMovement,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EaseOfMovement1'>
            },
            'SymmetricalTriangle': {
                'class': SymmetricalTriangle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SymmetricalTriangle'>
            }
        }),
        ('weights', {
            'EaseOfMovement': 1.0,
            'SymmetricalTriangle': 1.0
        })
    )
