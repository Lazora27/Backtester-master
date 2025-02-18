import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AverageLogRange_BollingerPercentB_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AverageLogRange und BollingerPercentB
    """
    
    params = (
        ('indicators', {
            'AverageLogRange': {
                'class': AverageLogRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageLogRange'>
            },
            'BollingerPercentB': {
                'class': BollingerPercentB,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerPercentB'>
            }
        }),
        ('weights', {
            'AverageLogRange': 1.0,
            'BollingerPercentB': 1.0
        })
    )
