import backtrader as bt
from ..base_strategy import FlexibleStrategy

class OrderFlowVolumeProfile_UlcerIndexVolume_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von OrderFlowVolumeProfile und UlcerIndexVolume
    """
    
    params = (
        ('indicators', {
            'OrderFlowVolumeProfile': {
                'class': OrderFlowVolumeProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OrderFlowVolumeProfile'>
            },
            'UlcerIndexVolume': {
                'class': UlcerIndexVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_UlcerIndexVolume'>
            }
        }),
        ('weights', {
            'OrderFlowVolumeProfile': 1.0,
            'UlcerIndexVolume': 1.0
        })
    )
