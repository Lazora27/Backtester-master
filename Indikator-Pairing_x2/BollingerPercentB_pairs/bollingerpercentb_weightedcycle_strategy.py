import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BollingerPercentB_WeightedCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BollingerPercentB und WeightedCycle
    """
    
    params = (
        ('indicators', {
            'BollingerPercentB': {
                'class': BollingerPercentB,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerPercentB'>
            },
            'WeightedCycle': {
                'class': WeightedCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeightedCycle'>
            }
        }),
        ('weights', {
            'BollingerPercentB': 1.0,
            'WeightedCycle': 1.0
        })
    )
