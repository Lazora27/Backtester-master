import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BollingerBands_VolumeRateOfChange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BollingerBands und VolumeRateOfChange
    """
    
    params = (
        ('indicators', {
            'BollingerBands': {
                'class': BollingerBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBands1'>
            },
            'VolumeRateOfChange': {
                'class': VolumeRateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeRateOfChange'>
            }
        }),
        ('weights', {
            'BollingerBands': 1.0,
            'VolumeRateOfChange': 1.0
        })
    )
