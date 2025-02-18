import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AverageTrueRange_OnBalanceVolume_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AverageTrueRange und OnBalanceVolume
    """
    
    params = (
        ('indicators', {
            'AverageTrueRange': {
                'class': AverageTrueRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageTrueRange1'>
            },
            'OnBalanceVolume': {
                'class': OnBalanceVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OnBalanceVolume'>
            }
        }),
        ('weights', {
            'AverageTrueRange': 1.0,
            'OnBalanceVolume': 1.0
        })
    )
