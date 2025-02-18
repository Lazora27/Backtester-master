import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PercentagePriceOscillator_FearGreedIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PercentagePriceOscillator und FearGreedIndex
    """
    
    params = (
        ('indicators', {
            'PercentagePriceOscillator': {
                'class': PercentagePriceOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PercentagePriceOscillator'>
            },
            'FearGreedIndex': {
                'class': FearGreedIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FearGreedIndex'>
            }
        }),
        ('weights', {
            'PercentagePriceOscillator': 1.0,
            'FearGreedIndex': 1.0
        })
    )
