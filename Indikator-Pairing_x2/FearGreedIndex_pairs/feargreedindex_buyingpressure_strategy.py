import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FearGreedIndex_BuyingPressure_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FearGreedIndex und BuyingPressure
    """
    
    params = (
        ('indicators', {
            'FearGreedIndex': {
                'class': FearGreedIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FearGreedIndex'>
            },
            'BuyingPressure': {
                'class': BuyingPressure,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BuyingPressure'>
            }
        }),
        ('weights', {
            'FearGreedIndex': 1.0,
            'BuyingPressure': 1.0
        })
    )
