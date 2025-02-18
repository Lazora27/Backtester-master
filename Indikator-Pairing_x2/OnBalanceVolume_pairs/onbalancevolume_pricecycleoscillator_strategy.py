import backtrader as bt
from ..base_strategy import FlexibleStrategy

class OnBalanceVolume_PriceCycleOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von OnBalanceVolume und PriceCycleOscillator
    """
    
    params = (
        ('indicators', {
            'OnBalanceVolume': {
                'class': OnBalanceVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OnBalanceVolume'>
            },
            'PriceCycleOscillator': {
                'class': PriceCycleOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceCycleOscillator'>
            }
        }),
        ('weights', {
            'OnBalanceVolume': 1.0,
            'PriceCycleOscillator': 1.0
        })
    )
