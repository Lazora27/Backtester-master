import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WeightedPutCallRatio_BollingerPercentB_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WeightedPutCallRatio und BollingerPercentB
    """
    
    params = (
        ('indicators', {
            'WeightedPutCallRatio': {
                'class': WeightedPutCallRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeightedPutCallRatio'>
            },
            'BollingerPercentB': {
                'class': BollingerPercentB,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerPercentB'>
            }
        }),
        ('weights', {
            'WeightedPutCallRatio': 1.0,
            'BollingerPercentB': 1.0
        })
    )
