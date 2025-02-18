import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannAngles_BollingerPercentB_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannAngles und BollingerPercentB
    """
    
    params = (
        ('indicators', {
            'GannAngles': {
                'class': GannAngles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannAngles1'>
            },
            'BollingerPercentB': {
                'class': BollingerPercentB,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerPercentB'>
            }
        }),
        ('weights', {
            'GannAngles': 1.0,
            'BollingerPercentB': 1.0
        })
    )
