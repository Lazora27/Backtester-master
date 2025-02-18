import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ChandeTrendScore_VolumeProfile_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ChandeTrendScore und VolumeProfile
    """
    
    params = (
        ('indicators', {
            'ChandeTrendScore': {
                'class': ChandeTrendScore,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChandeTrendScore'>
            },
            'VolumeProfile': {
                'class': VolumeProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeProfile'>
            }
        }),
        ('weights', {
            'ChandeTrendScore': 1.0,
            'VolumeProfile': 1.0
        })
    )
