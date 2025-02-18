import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ParabolicSAR_OnBalanceVolume_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ParabolicSAR und OnBalanceVolume
    """
    
    params = (
        ('indicators', {
            'ParabolicSAR': {
                'class': ParabolicSAR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ParabolicSAR'>
            },
            'OnBalanceVolume': {
                'class': OnBalanceVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OnBalanceVolume'>
            }
        }),
        ('weights', {
            'ParabolicSAR': 1.0,
            'OnBalanceVolume': 1.0
        })
    )
