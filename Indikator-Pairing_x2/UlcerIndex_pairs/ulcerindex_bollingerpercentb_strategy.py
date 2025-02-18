import backtrader as bt
from ..base_strategy import FlexibleStrategy

class UlcerIndex_BollingerPercentB_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von UlcerIndex und BollingerPercentB
    """
    
    params = (
        ('indicators', {
            'UlcerIndex': {
                'class': UlcerIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_UlcerIndex'>
            },
            'BollingerPercentB': {
                'class': BollingerPercentB,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerPercentB'>
            }
        }),
        ('weights', {
            'UlcerIndex': 1.0,
            'BollingerPercentB': 1.0
        })
    )
