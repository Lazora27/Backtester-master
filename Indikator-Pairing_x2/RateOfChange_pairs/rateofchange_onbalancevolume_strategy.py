import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RateOfChange_OnBalanceVolume_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RateOfChange und OnBalanceVolume
    """
    
    params = (
        ('indicators', {
            'RateOfChange': {
                'class': RateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RateOfChange1'>
            },
            'OnBalanceVolume': {
                'class': OnBalanceVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OnBalanceVolume'>
            }
        }),
        ('weights', {
            'RateOfChange': 1.0,
            'OnBalanceVolume': 1.0
        })
    )
