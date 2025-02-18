import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ChandeTrendScore_UlcerIndexVolume_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ChandeTrendScore und UlcerIndexVolume
    """
    
    params = (
        ('indicators', {
            'ChandeTrendScore': {
                'class': ChandeTrendScore,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChandeTrendScore'>
            },
            'UlcerIndexVolume': {
                'class': UlcerIndexVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_UlcerIndexVolume'>
            }
        }),
        ('weights', {
            'ChandeTrendScore': 1.0,
            'UlcerIndexVolume': 1.0
        })
    )
