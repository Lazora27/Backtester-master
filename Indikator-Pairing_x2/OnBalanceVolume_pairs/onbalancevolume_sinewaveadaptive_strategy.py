import backtrader as bt
from ..base_strategy import FlexibleStrategy

class OnBalanceVolume_SineWaveAdaptive_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von OnBalanceVolume und SineWaveAdaptive
    """
    
    params = (
        ('indicators', {
            'OnBalanceVolume': {
                'class': OnBalanceVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OnBalanceVolume'>
            },
            'SineWaveAdaptive': {
                'class': SineWaveAdaptive,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SineWaveAdaptive'>
            }
        }),
        ('weights', {
            'OnBalanceVolume': 1.0,
            'SineWaveAdaptive': 1.0
        })
    )
