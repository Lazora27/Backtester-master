import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BollingerPercentB_WeeklyCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BollingerPercentB und WeeklyCycle
    """
    
    params = (
        ('indicators', {
            'BollingerPercentB': {
                'class': BollingerPercentB,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerPercentB'>
            },
            'WeeklyCycle': {
                'class': WeeklyCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeeklyCycle'>
            }
        }),
        ('weights', {
            'BollingerPercentB': 1.0,
            'WeeklyCycle': 1.0
        })
    )
