import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BollingerPercentB_ParabolicTimePrice_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BollingerPercentB und ParabolicTimePrice
    """
    
    params = (
        ('indicators', {
            'BollingerPercentB': {
                'class': BollingerPercentB,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerPercentB'>
            },
            'ParabolicTimePrice': {
                'class': ParabolicTimePrice,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ParabolicTimePrice'>
            }
        }),
        ('weights', {
            'BollingerPercentB': 1.0,
            'ParabolicTimePrice': 1.0
        })
    )
