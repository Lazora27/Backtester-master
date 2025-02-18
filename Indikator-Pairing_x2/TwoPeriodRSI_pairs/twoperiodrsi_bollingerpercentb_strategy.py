import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TwoPeriodRSI_BollingerPercentB_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TwoPeriodRSI und BollingerPercentB
    """
    
    params = (
        ('indicators', {
            'TwoPeriodRSI': {
                'class': TwoPeriodRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TwoPeriodRSI'>
            },
            'BollingerPercentB': {
                'class': BollingerPercentB,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerPercentB'>
            }
        }),
        ('weights', {
            'TwoPeriodRSI': 1.0,
            'BollingerPercentB': 1.0
        })
    )
