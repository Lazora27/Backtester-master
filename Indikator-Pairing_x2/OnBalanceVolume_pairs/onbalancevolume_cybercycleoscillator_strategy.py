import backtrader as bt
from ..base_strategy import FlexibleStrategy

class OnBalanceVolume_CyberCycleOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von OnBalanceVolume und CyberCycleOscillator
    """
    
    params = (
        ('indicators', {
            'OnBalanceVolume': {
                'class': OnBalanceVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OnBalanceVolume'>
            },
            'CyberCycleOscillator': {
                'class': CyberCycleOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CyberCycleOscillator'>
            }
        }),
        ('weights', {
            'OnBalanceVolume': 1.0,
            'CyberCycleOscillator': 1.0
        })
    )
