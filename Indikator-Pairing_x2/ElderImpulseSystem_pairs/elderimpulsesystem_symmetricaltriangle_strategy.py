import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ElderImpulseSystem_SymmetricalTriangle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ElderImpulseSystem und SymmetricalTriangle
    """
    
    params = (
        ('indicators', {
            'ElderImpulseSystem': {
                'class': ElderImpulseSystem,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ElderImpulseSystem'>
            },
            'SymmetricalTriangle': {
                'class': SymmetricalTriangle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SymmetricalTriangle'>
            }
        }),
        ('weights', {
            'ElderImpulseSystem': 1.0,
            'SymmetricalTriangle': 1.0
        })
    )
