import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BollingerPercentB_MarketFacilitationIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BollingerPercentB und MarketFacilitationIndex
    """
    
    params = (
        ('indicators', {
            'BollingerPercentB': {
                'class': BollingerPercentB,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerPercentB'>
            },
            'MarketFacilitationIndex': {
                'class': MarketFacilitationIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketFacilitationIndex'>
            }
        }),
        ('weights', {
            'BollingerPercentB': 1.0,
            'MarketFacilitationIndex': 1.0
        })
    )
