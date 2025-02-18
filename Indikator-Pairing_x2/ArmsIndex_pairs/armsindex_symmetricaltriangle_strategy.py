import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ArmsIndex_SymmetricalTriangle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ArmsIndex und SymmetricalTriangle
    """
    
    params = (
        ('indicators', {
            'ArmsIndex': {
                'class': ArmsIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ArmsIndex'>
            },
            'SymmetricalTriangle': {
                'class': SymmetricalTriangle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SymmetricalTriangle'>
            }
        }),
        ('weights', {
            'ArmsIndex': 1.0,
            'SymmetricalTriangle': 1.0
        })
    )
