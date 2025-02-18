import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BollingerPercentB_HilbertTrendline_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BollingerPercentB und HilbertTrendline
    """
    
    params = (
        ('indicators', {
            'BollingerPercentB': {
                'class': BollingerPercentB,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerPercentB'>
            },
            'HilbertTrendline': {
                'class': HilbertTrendline,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertTrendline'>
            }
        }),
        ('weights', {
            'BollingerPercentB': 1.0,
            'HilbertTrendline': 1.0
        })
    )
