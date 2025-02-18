import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RelativeVolatilityIndex_DominantCycleOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RelativeVolatilityIndex und DominantCycleOscillator
    """
    
    params = (
        ('indicators', {
            'RelativeVolatilityIndex': {
                'class': RelativeVolatilityIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RelativeVolatilityIndex'>
            },
            'DominantCycleOscillator': {
                'class': DominantCycleOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DominantCycleOscillator'>
            }
        }),
        ('weights', {
            'RelativeVolatilityIndex': 1.0,
            'DominantCycleOscillator': 1.0
        })
    )
