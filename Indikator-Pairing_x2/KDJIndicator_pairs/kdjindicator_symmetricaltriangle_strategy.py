import backtrader as bt
from ..base_strategy import FlexibleStrategy

class KDJIndicator_SymmetricalTriangle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von KDJIndicator und SymmetricalTriangle
    """
    
    params = (
        ('indicators', {
            'KDJIndicator': {
                'class': KDJIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KDJIndicator'>
            },
            'SymmetricalTriangle': {
                'class': SymmetricalTriangle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SymmetricalTriangle'>
            }
        }),
        ('weights', {
            'KDJIndicator': 1.0,
            'SymmetricalTriangle': 1.0
        })
    )
