import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FearGreedIndex_PriceRateOfChange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FearGreedIndex und PriceRateOfChange
    """
    
    params = (
        ('indicators', {
            'FearGreedIndex': {
                'class': FearGreedIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FearGreedIndex'>
            },
            'PriceRateOfChange': {
                'class': PriceRateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceRateOfChange'>
            }
        }),
        ('weights', {
            'FearGreedIndex': 1.0,
            'PriceRateOfChange': 1.0
        })
    )
