import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ParabolicSAR_BollingerPercentB_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ParabolicSAR und BollingerPercentB
    """
    
    params = (
        ('indicators', {
            'ParabolicSAR': {
                'class': ParabolicSAR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ParabolicSAR'>
            },
            'BollingerPercentB': {
                'class': BollingerPercentB,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerPercentB'>
            }
        }),
        ('weights', {
            'ParabolicSAR': 1.0,
            'BollingerPercentB': 1.0
        })
    )
