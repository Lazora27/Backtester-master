import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RSIDivergence_BollingerPercentB_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RSIDivergence und BollingerPercentB
    """
    
    params = (
        ('indicators', {
            'RSIDivergence': {
                'class': RSIDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RSIDivergence'>
            },
            'BollingerPercentB': {
                'class': BollingerPercentB,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerPercentB'>
            }
        }),
        ('weights', {
            'RSIDivergence': 1.0,
            'BollingerPercentB': 1.0
        })
    )
