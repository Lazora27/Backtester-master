import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VolumeProfile_KeltnerBandWidth_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VolumeProfile und KeltnerBandWidth
    """
    
    params = (
        ('indicators', {
            'VolumeProfile': {
                'class': VolumeProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeProfile'>
            },
            'KeltnerBandWidth': {
                'class': KeltnerBandWidth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KeltnerBandWidth'>
            }
        }),
        ('weights', {
            'VolumeProfile': 1.0,
            'KeltnerBandWidth': 1.0
        })
    )
