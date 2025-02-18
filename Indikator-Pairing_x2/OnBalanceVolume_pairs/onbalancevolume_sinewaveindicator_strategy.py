import backtrader as bt
from ..base_strategy import FlexibleStrategy

class OnBalanceVolume_SineWaveIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von OnBalanceVolume und SineWaveIndicator
    """
    
    params = (
        ('indicators', {
            'OnBalanceVolume': {
                'class': OnBalanceVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OnBalanceVolume'>
            },
            'SineWaveIndicator': {
                'class': SineWaveIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SineWaveIndicator'>
            }
        }),
        ('weights', {
            'OnBalanceVolume': 1.0,
            'SineWaveIndicator': 1.0
        })
    )
