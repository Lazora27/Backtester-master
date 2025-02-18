import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BollingerPercentB_HilbertDominantCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BollingerPercentB und HilbertDominantCycle
    """
    
    params = (
        ('indicators', {
            'BollingerPercentB': {
                'class': BollingerPercentB,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerPercentB'>
            },
            'HilbertDominantCycle': {
                'class': HilbertDominantCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertDominantCycle'>
            }
        }),
        ('weights', {
            'BollingerPercentB': 1.0,
            'HilbertDominantCycle': 1.0
        })
    )
