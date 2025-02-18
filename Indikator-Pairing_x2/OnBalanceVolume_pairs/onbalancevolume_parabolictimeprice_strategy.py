import backtrader as bt
from ..base_strategy import FlexibleStrategy

class OnBalanceVolume_ParabolicTimePrice_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von OnBalanceVolume und ParabolicTimePrice
    """
    
    params = (
        ('indicators', {
            'OnBalanceVolume': {
                'class': OnBalanceVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OnBalanceVolume'>
            },
            'ParabolicTimePrice': {
                'class': ParabolicTimePrice,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ParabolicTimePrice'>
            }
        }),
        ('weights', {
            'OnBalanceVolume': 1.0,
            'ParabolicTimePrice': 1.0
        })
    )
