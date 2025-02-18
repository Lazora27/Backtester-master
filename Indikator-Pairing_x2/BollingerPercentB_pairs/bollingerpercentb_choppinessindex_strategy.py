import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BollingerPercentB_ChoppinessIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BollingerPercentB und ChoppinessIndex
    """
    
    params = (
        ('indicators', {
            'BollingerPercentB': {
                'class': BollingerPercentB,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerPercentB'>
            },
            'ChoppinessIndex': {
                'class': ChoppinessIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChoppinessIndex'>
            }
        }),
        ('weights', {
            'BollingerPercentB': 1.0,
            'ChoppinessIndex': 1.0
        })
    )
