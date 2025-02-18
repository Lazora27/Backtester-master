import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AutoSupportResistance_BollingerPercentB_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AutoSupportResistance und BollingerPercentB
    """
    
    params = (
        ('indicators', {
            'AutoSupportResistance': {
                'class': AutoSupportResistance,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AutoSupportResistance'>
            },
            'BollingerPercentB': {
                'class': BollingerPercentB,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerPercentB'>
            }
        }),
        ('weights', {
            'AutoSupportResistance': 1.0,
            'BollingerPercentB': 1.0
        })
    )
