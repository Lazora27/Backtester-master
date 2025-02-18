import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ChandeTrendScore_VolumeDelta_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ChandeTrendScore und VolumeDelta
    """
    
    params = (
        ('indicators', {
            'ChandeTrendScore': {
                'class': ChandeTrendScore,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChandeTrendScore'>
            },
            'VolumeDelta': {
                'class': VolumeDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeDelta'>
            }
        }),
        ('weights', {
            'ChandeTrendScore': 1.0,
            'VolumeDelta': 1.0
        })
    )
