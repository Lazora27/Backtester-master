import backtrader as bt
from ..base_strategy import FlexibleStrategy

class OnBalanceVolume_CCITurbo_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von OnBalanceVolume und CCITurbo
    """
    
    params = (
        ('indicators', {
            'OnBalanceVolume': {
                'class': OnBalanceVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OnBalanceVolume'>
            },
            'CCITurbo': {
                'class': CCITurbo,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CCITurbo'>
            }
        }),
        ('weights', {
            'OnBalanceVolume': 1.0,
            'CCITurbo': 1.0
        })
    )
