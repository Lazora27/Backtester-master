import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TrueStrengthIndex_BollingerPercentB_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TrueStrengthIndex und BollingerPercentB
    """
    
    params = (
        ('indicators', {
            'TrueStrengthIndex': {
                'class': TrueStrengthIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrueStrengthIndex'>
            },
            'BollingerPercentB': {
                'class': BollingerPercentB,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerPercentB'>
            }
        }),
        ('weights', {
            'TrueStrengthIndex': 1.0,
            'BollingerPercentB': 1.0
        })
    )
