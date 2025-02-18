import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RateOfChange_BollingerPercentB_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RateOfChange und BollingerPercentB
    """
    
    params = (
        ('indicators', {
            'RateOfChange': {
                'class': RateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RateOfChange1'>
            },
            'BollingerPercentB': {
                'class': BollingerPercentB,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerPercentB'>
            }
        }),
        ('weights', {
            'RateOfChange': 1.0,
            'BollingerPercentB': 1.0
        })
    )
