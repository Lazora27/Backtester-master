import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AdvancedCandlePattern_OnBalanceVolume_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AdvancedCandlePattern und OnBalanceVolume
    """
    
    params = (
        ('indicators', {
            'AdvancedCandlePattern': {
                'class': AdvancedCandlePattern,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdvancedCandlePattern'>
            },
            'OnBalanceVolume': {
                'class': OnBalanceVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OnBalanceVolume'>
            }
        }),
        ('weights', {
            'AdvancedCandlePattern': 1.0,
            'OnBalanceVolume': 1.0
        })
    )
