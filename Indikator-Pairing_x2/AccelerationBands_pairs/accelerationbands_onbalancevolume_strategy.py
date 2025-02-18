import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AccelerationBands_OnBalanceVolume_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AccelerationBands und OnBalanceVolume
    """
    
    params = (
        ('indicators', {
            'AccelerationBands': {
                'class': AccelerationBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AccelerationBands'>
            },
            'OnBalanceVolume': {
                'class': OnBalanceVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OnBalanceVolume'>
            }
        }),
        ('weights', {
            'AccelerationBands': 1.0,
            'OnBalanceVolume': 1.0
        })
    )
