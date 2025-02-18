import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BollingerBandWidth_VolumeRateOfChange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BollingerBandWidth und VolumeRateOfChange
    """
    
    params = (
        ('indicators', {
            'BollingerBandWidth': {
                'class': BollingerBandWidth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBandWidth'>
            },
            'VolumeRateOfChange': {
                'class': VolumeRateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeRateOfChange'>
            }
        }),
        ('weights', {
            'BollingerBandWidth': 1.0,
            'VolumeRateOfChange': 1.0
        })
    )
