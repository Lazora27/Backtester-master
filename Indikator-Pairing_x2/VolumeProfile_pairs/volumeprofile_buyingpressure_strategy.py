import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VolumeProfile_BuyingPressure_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VolumeProfile und BuyingPressure
    """
    
    params = (
        ('indicators', {
            'VolumeProfile': {
                'class': VolumeProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeProfile'>
            },
            'BuyingPressure': {
                'class': BuyingPressure,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BuyingPressure'>
            }
        }),
        ('weights', {
            'VolumeProfile': 1.0,
            'BuyingPressure': 1.0
        })
    )
