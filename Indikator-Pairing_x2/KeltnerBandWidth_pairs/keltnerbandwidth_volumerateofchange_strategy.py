import backtrader as bt
from ..base_strategy import FlexibleStrategy

class KeltnerBandWidth_VolumeRateOfChange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von KeltnerBandWidth und VolumeRateOfChange
    """
    
    params = (
        ('indicators', {
            'KeltnerBandWidth': {
                'class': KeltnerBandWidth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KeltnerBandWidth'>
            },
            'VolumeRateOfChange': {
                'class': VolumeRateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeRateOfChange'>
            }
        }),
        ('weights', {
            'KeltnerBandWidth': 1.0,
            'VolumeRateOfChange': 1.0
        })
    )
