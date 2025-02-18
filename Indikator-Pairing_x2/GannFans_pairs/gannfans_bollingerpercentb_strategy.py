import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannFans_BollingerPercentB_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannFans und BollingerPercentB
    """
    
    params = (
        ('indicators', {
            'GannFans': {
                'class': GannFans,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannFans'>
            },
            'BollingerPercentB': {
                'class': BollingerPercentB,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerPercentB'>
            }
        }),
        ('weights', {
            'GannFans': 1.0,
            'BollingerPercentB': 1.0
        })
    )
