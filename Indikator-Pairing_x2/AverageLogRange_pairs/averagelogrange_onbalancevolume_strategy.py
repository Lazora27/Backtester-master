import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AverageLogRange_OnBalanceVolume_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AverageLogRange und OnBalanceVolume
    """
    
    params = (
        ('indicators', {
            'AverageLogRange': {
                'class': AverageLogRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageLogRange'>
            },
            'OnBalanceVolume': {
                'class': OnBalanceVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OnBalanceVolume'>
            }
        }),
        ('weights', {
            'AverageLogRange': 1.0,
            'OnBalanceVolume': 1.0
        })
    )
