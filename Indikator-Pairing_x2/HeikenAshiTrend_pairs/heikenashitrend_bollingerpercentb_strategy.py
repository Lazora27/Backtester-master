import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HeikenAshiTrend_BollingerPercentB_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HeikenAshiTrend und BollingerPercentB
    """
    
    params = (
        ('indicators', {
            'HeikenAshiTrend': {
                'class': HeikenAshiTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HeikenAshiTrend'>
            },
            'BollingerPercentB': {
                'class': BollingerPercentB,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerPercentB'>
            }
        }),
        ('weights', {
            'HeikenAshiTrend': 1.0,
            'BollingerPercentB': 1.0
        })
    )
