import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WilliamsVIXFix_OnBalanceVolume_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WilliamsVIXFix und OnBalanceVolume
    """
    
    params = (
        ('indicators', {
            'WilliamsVIXFix': {
                'class': WilliamsVIXFix,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WilliamsVIXFix'>
            },
            'OnBalanceVolume': {
                'class': OnBalanceVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OnBalanceVolume'>
            }
        }),
        ('weights', {
            'WilliamsVIXFix': 1.0,
            'OnBalanceVolume': 1.0
        })
    )
