import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TrueRange_OnBalanceVolume_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TrueRange und OnBalanceVolume
    """
    
    params = (
        ('indicators', {
            'TrueRange': {
                'class': TrueRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrueRange1'>
            },
            'OnBalanceVolume': {
                'class': OnBalanceVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OnBalanceVolume'>
            }
        }),
        ('weights', {
            'TrueRange': 1.0,
            'OnBalanceVolume': 1.0
        })
    )
