import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BollingerPercentB_OpenInterest_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BollingerPercentB und OpenInterest
    """
    
    params = (
        ('indicators', {
            'BollingerPercentB': {
                'class': BollingerPercentB,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerPercentB'>
            },
            'OpenInterest': {
                'class': OpenInterest,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OpenInterest'>
            }
        }),
        ('weights', {
            'BollingerPercentB': 1.0,
            'OpenInterest': 1.0
        })
    )
