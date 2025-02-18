import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FractalChaosOscillator_ModifiedRSI_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FractalChaosOscillator und ModifiedRSI
    """
    
    params = (
        ('indicators', {
            'FractalChaosOscillator': {
                'class': FractalChaosOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FractalChaosOscillator'>
            },
            'ModifiedRSI': {
                'class': ModifiedRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ModifiedRSI'>
            }
        }),
        ('weights', {
            'FractalChaosOscillator': 1.0,
            'ModifiedRSI': 1.0
        })
    )
