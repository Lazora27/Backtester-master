import backtrader as bt
from ..base_strategy import FlexibleStrategy

class OnBalanceVolume_CyberCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von OnBalanceVolume und CyberCycle
    """
    
    params = (
        ('indicators', {
            'OnBalanceVolume': {
                'class': OnBalanceVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OnBalanceVolume'>
            },
            'CyberCycle': {
                'class': CyberCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CyberCycle'>
            }
        }),
        ('weights', {
            'OnBalanceVolume': 1.0,
            'CyberCycle': 1.0
        })
    )
