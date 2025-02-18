import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VolumeProfile_BollingerBandWidth_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VolumeProfile und BollingerBandWidth
    """
    
    params = (
        ('indicators', {
            'VolumeProfile': {
                'class': VolumeProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeProfile'>
            },
            'BollingerBandWidth': {
                'class': BollingerBandWidth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBandWidth'>
            }
        }),
        ('weights', {
            'VolumeProfile': 1.0,
            'BollingerBandWidth': 1.0
        })
    )
