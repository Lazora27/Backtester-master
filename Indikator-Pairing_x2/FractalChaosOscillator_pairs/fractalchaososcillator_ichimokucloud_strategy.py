import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FractalChaosOscillator_IchimokuCloud_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FractalChaosOscillator und IchimokuCloud
    """
    
    params = (
        ('indicators', {
            'FractalChaosOscillator': {
                'class': FractalChaosOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FractalChaosOscillator'>
            },
            'IchimokuCloud': {
                'class': IchimokuCloud,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_IchimokuCloud'>
            }
        }),
        ('weights', {
            'FractalChaosOscillator': 1.0,
            'IchimokuCloud': 1.0
        })
    )
