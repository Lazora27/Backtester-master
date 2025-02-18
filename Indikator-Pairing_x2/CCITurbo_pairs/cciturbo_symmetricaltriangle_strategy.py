import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CCITurbo_SymmetricalTriangle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CCITurbo und SymmetricalTriangle
    """
    
    params = (
        ('indicators', {
            'CCITurbo': {
                'class': CCITurbo,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CCITurbo'>
            },
            'SymmetricalTriangle': {
                'class': SymmetricalTriangle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SymmetricalTriangle'>
            }
        }),
        ('weights', {
            'CCITurbo': 1.0,
            'SymmetricalTriangle': 1.0
        })
    )
