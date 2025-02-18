import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WolfeWaves_SymmetricalTriangle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WolfeWaves und SymmetricalTriangle
    """
    
    params = (
        ('indicators', {
            'WolfeWaves': {
                'class': WolfeWaves,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WolfeWaves'>
            },
            'SymmetricalTriangle': {
                'class': SymmetricalTriangle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SymmetricalTriangle'>
            }
        }),
        ('weights', {
            'WolfeWaves': 1.0,
            'SymmetricalTriangle': 1.0
        })
    )
