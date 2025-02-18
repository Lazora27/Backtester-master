import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MurreyMathSignals_BollingerPercentB_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MurreyMathSignals und BollingerPercentB
    """
    
    params = (
        ('indicators', {
            'MurreyMathSignals': {
                'class': MurreyMathSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MurreyMathSignals'>
            },
            'BollingerPercentB': {
                'class': BollingerPercentB,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerPercentB'>
            }
        }),
        ('weights', {
            'MurreyMathSignals': 1.0,
            'BollingerPercentB': 1.0
        })
    )
