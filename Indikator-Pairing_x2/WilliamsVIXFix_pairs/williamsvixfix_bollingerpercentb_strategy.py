import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WilliamsVIXFix_BollingerPercentB_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WilliamsVIXFix und BollingerPercentB
    """
    
    params = (
        ('indicators', {
            'WilliamsVIXFix': {
                'class': WilliamsVIXFix,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WilliamsVIXFix'>
            },
            'BollingerPercentB': {
                'class': BollingerPercentB,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerPercentB'>
            }
        }),
        ('weights', {
            'WilliamsVIXFix': 1.0,
            'BollingerPercentB': 1.0
        })
    )
