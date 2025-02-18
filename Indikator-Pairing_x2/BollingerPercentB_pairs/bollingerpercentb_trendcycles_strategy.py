import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BollingerPercentB_TrendCycles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BollingerPercentB und TrendCycles
    """
    
    params = (
        ('indicators', {
            'BollingerPercentB': {
                'class': BollingerPercentB,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerPercentB'>
            },
            'TrendCycles': {
                'class': TrendCycles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrendCycles'>
            }
        }),
        ('weights', {
            'BollingerPercentB': 1.0,
            'TrendCycles': 1.0
        })
    )
