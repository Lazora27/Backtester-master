import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FractalChaosOscillator_OnBalanceVolume_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FractalChaosOscillator und OnBalanceVolume
    """
    
    params = (
        ('indicators', {
            'FractalChaosOscillator': {
                'class': FractalChaosOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FractalChaosOscillator'>
            },
            'OnBalanceVolume': {
                'class': OnBalanceVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OnBalanceVolume'>
            }
        }),
        ('weights', {
            'FractalChaosOscillator': 1.0,
            'OnBalanceVolume': 1.0
        })
    )
