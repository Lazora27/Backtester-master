import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ElderImpulseSystem_EhlersDecycler_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ElderImpulseSystem und EhlersDecycler
    """
    
    params = (
        ('indicators', {
            'ElderImpulseSystem': {
                'class': ElderImpulseSystem,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ElderImpulseSystem'>
            },
            'EhlersDecycler': {
                'class': EhlersDecycler,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EhlersDecycler'>
            }
        }),
        ('weights', {
            'ElderImpulseSystem': 1.0,
            'EhlersDecycler': 1.0
        })
    )
