import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VortexIndicator_OnBalanceVolume_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VortexIndicator und OnBalanceVolume
    """
    
    params = (
        ('indicators', {
            'VortexIndicator': {
                'class': VortexIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VortexIndicator'>
            },
            'OnBalanceVolume': {
                'class': OnBalanceVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OnBalanceVolume'>
            }
        }),
        ('weights', {
            'VortexIndicator': 1.0,
            'OnBalanceVolume': 1.0
        })
    )
