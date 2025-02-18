import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ElderImpulseSystem_KeltnerBandWidth_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ElderImpulseSystem und KeltnerBandWidth
    """
    
    params = (
        ('indicators', {
            'ElderImpulseSystem': {
                'class': ElderImpulseSystem,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ElderImpulseSystem'>
            },
            'KeltnerBandWidth': {
                'class': KeltnerBandWidth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KeltnerBandWidth'>
            }
        }),
        ('weights', {
            'ElderImpulseSystem': 1.0,
            'KeltnerBandWidth': 1.0
        })
    )
