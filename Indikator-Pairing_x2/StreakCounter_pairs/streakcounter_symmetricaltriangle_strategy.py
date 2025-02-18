import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StreakCounter_SymmetricalTriangle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StreakCounter und SymmetricalTriangle
    """
    
    params = (
        ('indicators', {
            'StreakCounter': {
                'class': StreakCounter,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StreakCounter'>
            },
            'SymmetricalTriangle': {
                'class': SymmetricalTriangle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SymmetricalTriangle'>
            }
        }),
        ('weights', {
            'StreakCounter': 1.0,
            'SymmetricalTriangle': 1.0
        })
    )
