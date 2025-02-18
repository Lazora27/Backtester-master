import backtrader as bt
from ..base_strategy import FlexibleStrategy

class NVISignals_VolumeProfile_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von NVISignals und VolumeProfile
    """
    
    params = (
        ('indicators', {
            'NVISignals': {
                'class': NVISignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_NVISignals'>
            },
            'VolumeProfile': {
                'class': VolumeProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeProfile'>
            }
        }),
        ('weights', {
            'NVISignals': 1.0,
            'VolumeProfile': 1.0
        })
    )
