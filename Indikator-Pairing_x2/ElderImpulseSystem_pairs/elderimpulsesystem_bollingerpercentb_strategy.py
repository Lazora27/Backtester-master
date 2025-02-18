import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ElderImpulseSystem_BollingerPercentB_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ElderImpulseSystem und BollingerPercentB
    """
    
    params = (
        ('indicators', {
            'ElderImpulseSystem': {
                'class': ElderImpulseSystem,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ElderImpulseSystem'>
            },
            'BollingerPercentB': {
                'class': BollingerPercentB,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerPercentB'>
            }
        }),
        ('weights', {
            'ElderImpulseSystem': 1.0,
            'BollingerPercentB': 1.0
        })
    )
