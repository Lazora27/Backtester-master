import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VolumeProfile_BollingerBandSqueeze_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VolumeProfile und BollingerBandSqueeze
    """
    
    params = (
        ('indicators', {
            'VolumeProfile': {
                'class': VolumeProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeProfile'>
            },
            'BollingerBandSqueeze': {
                'class': BollingerBandSqueeze,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBandSqueeze'>
            }
        }),
        ('weights', {
            'VolumeProfile': 1.0,
            'BollingerBandSqueeze': 1.0
        })
    )
