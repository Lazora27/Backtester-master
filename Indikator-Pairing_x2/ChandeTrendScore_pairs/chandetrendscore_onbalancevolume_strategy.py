import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ChandeTrendScore_OnBalanceVolume_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ChandeTrendScore und OnBalanceVolume
    """
    
    params = (
        ('indicators', {
            'ChandeTrendScore': {
                'class': ChandeTrendScore,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChandeTrendScore'>
            },
            'OnBalanceVolume': {
                'class': OnBalanceVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OnBalanceVolume'>
            }
        }),
        ('weights', {
            'ChandeTrendScore': 1.0,
            'OnBalanceVolume': 1.0
        })
    )
