import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PriceDelta_VolumeProfile_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PriceDelta und VolumeProfile
    """
    
    params = (
        ('indicators', {
            'PriceDelta': {
                'class': PriceDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceDelta'>
            },
            'VolumeProfile': {
                'class': VolumeProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeProfile'>
            }
        }),
        ('weights', {
            'PriceDelta': 1.0,
            'VolumeProfile': 1.0
        })
    )
