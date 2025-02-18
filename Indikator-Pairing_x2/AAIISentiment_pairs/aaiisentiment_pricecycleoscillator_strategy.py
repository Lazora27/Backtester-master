import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AAIISentiment_PriceCycleOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AAIISentiment und PriceCycleOscillator
    """
    
    params = (
        ('indicators', {
            'AAIISentiment': {
                'class': AAIISentiment,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AAIISentiment'>
            },
            'PriceCycleOscillator': {
                'class': PriceCycleOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceCycleOscillator'>
            }
        }),
        ('weights', {
            'AAIISentiment': 1.0,
            'PriceCycleOscillator': 1.0
        })
    )
