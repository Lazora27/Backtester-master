import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AverageDirectionalIndex_BollingerPercentB_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AverageDirectionalIndex und BollingerPercentB
    """
    
    params = (
        ('indicators', {
            'AverageDirectionalIndex': {
                'class': AverageDirectionalIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageDirectionalIndex'>
            },
            'BollingerPercentB': {
                'class': BollingerPercentB,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerPercentB'>
            }
        }),
        ('weights', {
            'AverageDirectionalIndex': 1.0,
            'BollingerPercentB': 1.0
        })
    )
