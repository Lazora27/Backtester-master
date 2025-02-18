import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BollingerBandSqueeze_VolumeRateOfChange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BollingerBandSqueeze und VolumeRateOfChange
    """
    
    params = (
        ('indicators', {
            'BollingerBandSqueeze': {
                'class': BollingerBandSqueeze,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBandSqueeze'>
            },
            'VolumeRateOfChange': {
                'class': VolumeRateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeRateOfChange'>
            }
        }),
        ('weights', {
            'BollingerBandSqueeze': 1.0,
            'VolumeRateOfChange': 1.0
        })
    )
