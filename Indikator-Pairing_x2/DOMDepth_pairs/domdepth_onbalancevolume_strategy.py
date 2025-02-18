import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DOMDepth_OnBalanceVolume_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DOMDepth und OnBalanceVolume
    """
    
    params = (
        ('indicators', {
            'DOMDepth': {
                'class': DOMDepth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DOMDepth'>
            },
            'OnBalanceVolume': {
                'class': OnBalanceVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OnBalanceVolume'>
            }
        }),
        ('weights', {
            'DOMDepth': 1.0,
            'OnBalanceVolume': 1.0
        })
    )
