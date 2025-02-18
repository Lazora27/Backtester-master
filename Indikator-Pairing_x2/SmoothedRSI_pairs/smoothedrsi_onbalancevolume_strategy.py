import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SmoothedRSI_OnBalanceVolume_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SmoothedRSI und OnBalanceVolume
    """
    
    params = (
        ('indicators', {
            'SmoothedRSI': {
                'class': SmoothedRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmoothedRSI'>
            },
            'OnBalanceVolume': {
                'class': OnBalanceVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OnBalanceVolume'>
            }
        }),
        ('weights', {
            'SmoothedRSI': 1.0,
            'OnBalanceVolume': 1.0
        })
    )
