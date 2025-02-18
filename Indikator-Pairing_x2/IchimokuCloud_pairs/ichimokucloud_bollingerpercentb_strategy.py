import backtrader as bt
from ..base_strategy import FlexibleStrategy

class IchimokuCloud_BollingerPercentB_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von IchimokuCloud und BollingerPercentB
    """
    
    params = (
        ('indicators', {
            'IchimokuCloud': {
                'class': IchimokuCloud,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_IchimokuCloud'>
            },
            'BollingerPercentB': {
                'class': BollingerPercentB,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerPercentB'>
            }
        }),
        ('weights', {
            'IchimokuCloud': 1.0,
            'BollingerPercentB': 1.0
        })
    )
