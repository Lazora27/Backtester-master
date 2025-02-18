import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ElderImpulseSystem_WolfeWaves_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ElderImpulseSystem und WolfeWaves
    """
    
    params = (
        ('indicators', {
            'ElderImpulseSystem': {
                'class': ElderImpulseSystem,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ElderImpulseSystem'>
            },
            'WolfeWaves': {
                'class': WolfeWaves,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WolfeWaves'>
            }
        }),
        ('weights', {
            'ElderImpulseSystem': 1.0,
            'WolfeWaves': 1.0
        })
    )
