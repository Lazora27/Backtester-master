import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AutoHarmonicPattern_OnBalanceVolume_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AutoHarmonicPattern und OnBalanceVolume
    """
    
    params = (
        ('indicators', {
            'AutoHarmonicPattern': {
                'class': AutoHarmonicPattern,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AutoHarmonicPattern'>
            },
            'OnBalanceVolume': {
                'class': OnBalanceVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OnBalanceVolume'>
            }
        }),
        ('weights', {
            'AutoHarmonicPattern': 1.0,
            'OnBalanceVolume': 1.0
        })
    )
