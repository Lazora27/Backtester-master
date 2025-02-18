import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TrueRange_BollingerPercentB_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TrueRange und BollingerPercentB
    """
    
    params = (
        ('indicators', {
            'TrueRange': {
                'class': TrueRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrueRange1'>
            },
            'BollingerPercentB': {
                'class': BollingerPercentB,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerPercentB'>
            }
        }),
        ('weights', {
            'TrueRange': 1.0,
            'BollingerPercentB': 1.0
        })
    )
