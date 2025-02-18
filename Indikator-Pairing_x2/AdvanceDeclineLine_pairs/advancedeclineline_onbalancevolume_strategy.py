import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AdvanceDeclineLine_OnBalanceVolume_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AdvanceDeclineLine und OnBalanceVolume
    """
    
    params = (
        ('indicators', {
            'AdvanceDeclineLine': {
                'class': AdvanceDeclineLine,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdvanceDeclineLine'>
            },
            'OnBalanceVolume': {
                'class': OnBalanceVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OnBalanceVolume'>
            }
        }),
        ('weights', {
            'AdvanceDeclineLine': 1.0,
            'OnBalanceVolume': 1.0
        })
    )
