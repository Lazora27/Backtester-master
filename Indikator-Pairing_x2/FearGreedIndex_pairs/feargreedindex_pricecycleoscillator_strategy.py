import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FearGreedIndex_PriceCycleOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FearGreedIndex und PriceCycleOscillator
    """
    
    params = (
        ('indicators', {
            'FearGreedIndex': {
                'class': FearGreedIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FearGreedIndex'>
            },
            'PriceCycleOscillator': {
                'class': PriceCycleOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceCycleOscillator'>
            }
        }),
        ('weights', {
            'FearGreedIndex': 1.0,
            'PriceCycleOscillator': 1.0
        })
    )
