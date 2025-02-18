import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BollingerPercentB_LiquidityIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BollingerPercentB und LiquidityIndex
    """
    
    params = (
        ('indicators', {
            'BollingerPercentB': {
                'class': BollingerPercentB,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerPercentB'>
            },
            'LiquidityIndex': {
                'class': LiquidityIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LiquidityIndex'>
            }
        }),
        ('weights', {
            'BollingerPercentB': 1.0,
            'LiquidityIndex': 1.0
        })
    )
