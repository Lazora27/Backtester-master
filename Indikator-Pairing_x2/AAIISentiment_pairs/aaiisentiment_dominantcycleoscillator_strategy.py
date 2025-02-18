import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AAIISentiment_DominantCycleOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AAIISentiment und DominantCycleOscillator
    """
    
    params = (
        ('indicators', {
            'AAIISentiment': {
                'class': AAIISentiment,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AAIISentiment'>
            },
            'DominantCycleOscillator': {
                'class': DominantCycleOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DominantCycleOscillator'>
            }
        }),
        ('weights', {
            'AAIISentiment': 1.0,
            'DominantCycleOscillator': 1.0
        })
    )
