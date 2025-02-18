import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ExtensionProjections_OnBalanceVolume_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ExtensionProjections und OnBalanceVolume
    """
    
    params = (
        ('indicators', {
            'ExtensionProjections': {
                'class': ExtensionProjections,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ExtensionProjections'>
            },
            'OnBalanceVolume': {
                'class': OnBalanceVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OnBalanceVolume'>
            }
        }),
        ('weights', {
            'ExtensionProjections': 1.0,
            'OnBalanceVolume': 1.0
        })
    )
