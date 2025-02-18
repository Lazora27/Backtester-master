import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CenterOfGravity_SymmetricalTriangle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CenterOfGravity und SymmetricalTriangle
    """
    
    params = (
        ('indicators', {
            'CenterOfGravity': {
                'class': CenterOfGravity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CenterOfGravity'>
            },
            'SymmetricalTriangle': {
                'class': SymmetricalTriangle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SymmetricalTriangle'>
            }
        }),
        ('weights', {
            'CenterOfGravity': 1.0,
            'SymmetricalTriangle': 1.0
        })
    )
