import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BollingerPercentB_TimeCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BollingerPercentB und TimeCycle
    """
    
    params = (
        ('indicators', {
            'BollingerPercentB': {
                'class': BollingerPercentB,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerPercentB'>
            },
            'TimeCycle': {
                'class': TimeCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeCycle'>
            }
        }),
        ('weights', {
            'BollingerPercentB': 1.0,
            'TimeCycle': 1.0
        })
    )
