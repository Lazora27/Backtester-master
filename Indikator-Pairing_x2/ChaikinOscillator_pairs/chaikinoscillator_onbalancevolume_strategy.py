import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ChaikinOscillator_OnBalanceVolume_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ChaikinOscillator und OnBalanceVolume
    """
    
    params = (
        ('indicators', {
            'ChaikinOscillator': {
                'class': ChaikinOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChaikinOscillator'>
            },
            'OnBalanceVolume': {
                'class': OnBalanceVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OnBalanceVolume'>
            }
        }),
        ('weights', {
            'ChaikinOscillator': 1.0,
            'OnBalanceVolume': 1.0
        })
    )
