import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ElderImpulseSystem_BollingerBandWidth_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ElderImpulseSystem und BollingerBandWidth
    """
    
    params = (
        ('indicators', {
            'ElderImpulseSystem': {
                'class': ElderImpulseSystem,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ElderImpulseSystem'>
            },
            'BollingerBandWidth': {
                'class': BollingerBandWidth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBandWidth'>
            }
        }),
        ('weights', {
            'ElderImpulseSystem': 1.0,
            'BollingerBandWidth': 1.0
        })
    )
