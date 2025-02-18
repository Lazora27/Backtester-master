import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ElderImpulseSystem_PivotPoints_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ElderImpulseSystem und PivotPoints
    """
    
    params = (
        ('indicators', {
            'ElderImpulseSystem': {
                'class': ElderImpulseSystem,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ElderImpulseSystem'>
            },
            'PivotPoints': {
                'class': PivotPoints,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PivotPoints'>
            }
        }),
        ('weights', {
            'ElderImpulseSystem': 1.0,
            'PivotPoints': 1.0
        })
    )
