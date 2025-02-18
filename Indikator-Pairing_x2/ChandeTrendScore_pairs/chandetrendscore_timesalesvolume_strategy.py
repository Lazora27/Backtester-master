import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ChandeTrendScore_TimeSalesVolume_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ChandeTrendScore und TimeSalesVolume
    """
    
    params = (
        ('indicators', {
            'ChandeTrendScore': {
                'class': ChandeTrendScore,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChandeTrendScore'>
            },
            'TimeSalesVolume': {
                'class': TimeSalesVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeSalesVolume'>
            }
        }),
        ('weights', {
            'ChandeTrendScore': 1.0,
            'TimeSalesVolume': 1.0
        })
    )
