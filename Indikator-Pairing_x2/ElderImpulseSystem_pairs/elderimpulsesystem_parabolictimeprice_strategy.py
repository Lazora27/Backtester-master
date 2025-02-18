import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ElderImpulseSystem_ParabolicTimePrice_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ElderImpulseSystem und ParabolicTimePrice
    """
    
    params = (
        ('indicators', {
            'ElderImpulseSystem': {
                'class': ElderImpulseSystem,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ElderImpulseSystem'>
            },
            'ParabolicTimePrice': {
                'class': ParabolicTimePrice,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ParabolicTimePrice'>
            }
        }),
        ('weights', {
            'ElderImpulseSystem': 1.0,
            'ParabolicTimePrice': 1.0
        })
    )
