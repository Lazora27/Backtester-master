import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ElderImpulseSystem_GannSquares_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ElderImpulseSystem und GannSquares
    """
    
    params = (
        ('indicators', {
            'ElderImpulseSystem': {
                'class': ElderImpulseSystem,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ElderImpulseSystem'>
            },
            'GannSquares': {
                'class': GannSquares,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannSquares'>
            }
        }),
        ('weights', {
            'ElderImpulseSystem': 1.0,
            'GannSquares': 1.0
        })
    )
