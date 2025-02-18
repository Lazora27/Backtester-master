import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FractalChaosOscillator_DemandIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FractalChaosOscillator und DemandIndex
    """
    
    params = (
        ('indicators', {
            'FractalChaosOscillator': {
                'class': FractalChaosOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FractalChaosOscillator'>
            },
            'DemandIndex': {
                'class': DemandIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DemandIndex'>
            }
        }),
        ('weights', {
            'FractalChaosOscillator': 1.0,
            'DemandIndex': 1.0
        })
    )
