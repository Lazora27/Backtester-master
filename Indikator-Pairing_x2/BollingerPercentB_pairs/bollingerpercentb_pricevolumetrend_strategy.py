import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BollingerPercentB_PriceVolumeTrend_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BollingerPercentB und PriceVolumeTrend
    """
    
    params = (
        ('indicators', {
            'BollingerPercentB': {
                'class': BollingerPercentB,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerPercentB'>
            },
            'PriceVolumeTrend': {
                'class': PriceVolumeTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceVolumeTrend'>
            }
        }),
        ('weights', {
            'BollingerPercentB': 1.0,
            'PriceVolumeTrend': 1.0
        })
    )
