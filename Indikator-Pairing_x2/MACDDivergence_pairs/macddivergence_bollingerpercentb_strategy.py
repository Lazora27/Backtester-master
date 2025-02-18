import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDDivergence_BollingerPercentB_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDDivergence und BollingerPercentB
    """
    
    params = (
        ('indicators', {
            'MACDDivergence': {
                'class': MACDDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDDivergence'>
            },
            'BollingerPercentB': {
                'class': BollingerPercentB,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerPercentB'>
            }
        }),
        ('weights', {
            'MACDDivergence': 1.0,
            'BollingerPercentB': 1.0
        })
    )
