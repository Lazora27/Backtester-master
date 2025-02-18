import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PivotPoints_OnBalanceVolume_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PivotPoints und OnBalanceVolume
    """
    
    params = (
        ('indicators', {
            'PivotPoints': {
                'class': PivotPoints,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PivotPoints'>
            },
            'OnBalanceVolume': {
                'class': OnBalanceVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OnBalanceVolume'>
            }
        }),
        ('weights', {
            'PivotPoints': 1.0,
            'OnBalanceVolume': 1.0
        })
    )
