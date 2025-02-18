import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VolumeProfile_PriceVolumeTrend_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VolumeProfile und PriceVolumeTrend
    """
    
    params = (
        ('indicators', {
            'VolumeProfile': {
                'class': VolumeProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeProfile'>
            },
            'PriceVolumeTrend': {
                'class': PriceVolumeTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceVolumeTrend'>
            }
        }),
        ('weights', {
            'VolumeProfile': 1.0,
            'PriceVolumeTrend': 1.0
        })
    )
