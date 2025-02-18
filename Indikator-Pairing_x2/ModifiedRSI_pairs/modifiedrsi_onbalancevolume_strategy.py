import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ModifiedRSI_OnBalanceVolume_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ModifiedRSI und OnBalanceVolume
    """
    
    params = (
        ('indicators', {
            'ModifiedRSI': {
                'class': ModifiedRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ModifiedRSI'>
            },
            'OnBalanceVolume': {
                'class': OnBalanceVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OnBalanceVolume'>
            }
        }),
        ('weights', {
            'ModifiedRSI': 1.0,
            'OnBalanceVolume': 1.0
        })
    )
