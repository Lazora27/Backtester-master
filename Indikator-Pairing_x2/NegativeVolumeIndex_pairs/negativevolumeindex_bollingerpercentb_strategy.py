import backtrader as bt
from ..base_strategy import FlexibleStrategy

class NegativeVolumeIndex_BollingerPercentB_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von NegativeVolumeIndex und BollingerPercentB
    """
    
    params = (
        ('indicators', {
            'NegativeVolumeIndex': {
                'class': NegativeVolumeIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_NegativeVolumeIndex'>
            },
            'BollingerPercentB': {
                'class': BollingerPercentB,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerPercentB'>
            }
        }),
        ('weights', {
            'NegativeVolumeIndex': 1.0,
            'BollingerPercentB': 1.0
        })
    )
