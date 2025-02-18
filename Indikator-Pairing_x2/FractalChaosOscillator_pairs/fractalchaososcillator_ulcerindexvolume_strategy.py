import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FractalChaosOscillator_UlcerIndexVolume_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FractalChaosOscillator und UlcerIndexVolume
    """
    
    params = (
        ('indicators', {
            'FractalChaosOscillator': {
                'class': FractalChaosOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FractalChaosOscillator'>
            },
            'UlcerIndexVolume': {
                'class': UlcerIndexVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_UlcerIndexVolume'>
            }
        }),
        ('weights', {
            'FractalChaosOscillator': 1.0,
            'UlcerIndexVolume': 1.0
        })
    )
