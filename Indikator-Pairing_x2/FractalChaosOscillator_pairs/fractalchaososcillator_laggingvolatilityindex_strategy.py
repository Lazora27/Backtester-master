import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FractalChaosOscillator_LaggingVolatilityIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FractalChaosOscillator und LaggingVolatilityIndex
    """
    
    params = (
        ('indicators', {
            'FractalChaosOscillator': {
                'class': FractalChaosOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FractalChaosOscillator'>
            },
            'LaggingVolatilityIndex': {
                'class': LaggingVolatilityIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LaggingVolatilityIndex'>
            }
        }),
        ('weights', {
            'FractalChaosOscillator': 1.0,
            'LaggingVolatilityIndex': 1.0
        })
    )
