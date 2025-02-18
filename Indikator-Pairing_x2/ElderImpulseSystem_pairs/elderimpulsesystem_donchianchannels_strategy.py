import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ElderImpulseSystem_DonchianChannels_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ElderImpulseSystem und DonchianChannels
    """
    
    params = (
        ('indicators', {
            'ElderImpulseSystem': {
                'class': ElderImpulseSystem,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ElderImpulseSystem'>
            },
            'DonchianChannels': {
                'class': DonchianChannels,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DonchianChannels'>
            }
        }),
        ('weights', {
            'ElderImpulseSystem': 1.0,
            'DonchianChannels': 1.0
        })
    )
