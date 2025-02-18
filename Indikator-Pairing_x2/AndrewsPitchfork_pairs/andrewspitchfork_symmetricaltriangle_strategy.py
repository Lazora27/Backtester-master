import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AndrewsPitchfork_SymmetricalTriangle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AndrewsPitchfork und SymmetricalTriangle
    """
    
    params = (
        ('indicators', {
            'AndrewsPitchfork': {
                'class': AndrewsPitchfork,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AndrewsPitchfork'>
            },
            'SymmetricalTriangle': {
                'class': SymmetricalTriangle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SymmetricalTriangle'>
            }
        }),
        ('weights', {
            'AndrewsPitchfork': 1.0,
            'SymmetricalTriangle': 1.0
        })
    )
