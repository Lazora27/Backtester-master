import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AwesomeOscillator_OnBalanceVolume_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AwesomeOscillator und OnBalanceVolume
    """
    
    params = (
        ('indicators', {
            'AwesomeOscillator': {
                'class': AwesomeOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AwesomeOscillator1'>
            },
            'OnBalanceVolume': {
                'class': OnBalanceVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OnBalanceVolume'>
            }
        }),
        ('weights', {
            'AwesomeOscillator': 1.0,
            'OnBalanceVolume': 1.0
        })
    )
