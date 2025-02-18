import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FisherTransform_BollingerPercentB_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FisherTransform und BollingerPercentB
    """
    
    params = (
        ('indicators', {
            'FisherTransform': {
                'class': FisherTransform,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FisherTransform'>
            },
            'BollingerPercentB': {
                'class': BollingerPercentB,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerPercentB'>
            }
        }),
        ('weights', {
            'FisherTransform': 1.0,
            'BollingerPercentB': 1.0
        })
    )
