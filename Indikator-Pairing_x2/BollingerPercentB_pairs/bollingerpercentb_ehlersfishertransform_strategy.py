import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BollingerPercentB_EhlersFisherTransform_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BollingerPercentB und EhlersFisherTransform
    """
    
    params = (
        ('indicators', {
            'BollingerPercentB': {
                'class': BollingerPercentB,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerPercentB'>
            },
            'EhlersFisherTransform': {
                'class': EhlersFisherTransform,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EhlersFisherTransform'>
            }
        }),
        ('weights', {
            'BollingerPercentB': 1.0,
            'EhlersFisherTransform': 1.0
        })
    )
