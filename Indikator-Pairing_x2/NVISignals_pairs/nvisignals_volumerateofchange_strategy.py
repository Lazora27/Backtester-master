import backtrader as bt
from ..base_strategy import FlexibleStrategy

class NVISignals_VolumeRateOfChange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von NVISignals und VolumeRateOfChange
    """
    
    params = (
        ('indicators', {
            'NVISignals': {
                'class': NVISignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_NVISignals'>
            },
            'VolumeRateOfChange': {
                'class': VolumeRateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeRateOfChange'>
            }
        }),
        ('weights', {
            'NVISignals': 1.0,
            'VolumeRateOfChange': 1.0
        })
    )
