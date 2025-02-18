import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TrendExhaustion_VolumeProfile_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TrendExhaustion und VolumeProfile
    """
    
    params = (
        ('indicators', {
            'TrendExhaustion': {
                'class': TrendExhaustion,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrendExhaustion'>
            },
            'VolumeProfile': {
                'class': VolumeProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeProfile'>
            }
        }),
        ('weights', {
            'TrendExhaustion': 1.0,
            'VolumeProfile': 1.0
        })
    )
