import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PositiveVolumeIndex_BollingerPercentB_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PositiveVolumeIndex und BollingerPercentB
    """
    
    params = (
        ('indicators', {
            'PositiveVolumeIndex': {
                'class': PositiveVolumeIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PositiveVolumeIndex'>
            },
            'BollingerPercentB': {
                'class': BollingerPercentB,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerPercentB'>
            }
        }),
        ('weights', {
            'PositiveVolumeIndex': 1.0,
            'BollingerPercentB': 1.0
        })
    )
