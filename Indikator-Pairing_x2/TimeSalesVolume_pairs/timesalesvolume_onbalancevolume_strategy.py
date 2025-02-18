import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TimeSalesVolume_OnBalanceVolume_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TimeSalesVolume und OnBalanceVolume
    """
    
    params = (
        ('indicators', {
            'TimeSalesVolume': {
                'class': TimeSalesVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeSalesVolume'>
            },
            'OnBalanceVolume': {
                'class': OnBalanceVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OnBalanceVolume'>
            }
        }),
        ('weights', {
            'TimeSalesVolume': 1.0,
            'OnBalanceVolume': 1.0
        })
    )
