import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PutCallRatio_BollingerPercentB_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PutCallRatio und BollingerPercentB
    """
    
    params = (
        ('indicators', {
            'PutCallRatio': {
                'class': PutCallRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PutCallRatio1'>
            },
            'BollingerPercentB': {
                'class': BollingerPercentB,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerPercentB'>
            }
        }),
        ('weights', {
            'PutCallRatio': 1.0,
            'BollingerPercentB': 1.0
        })
    )
