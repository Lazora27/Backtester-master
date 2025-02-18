import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VolumeDelta_BollingerPercentB_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VolumeDelta und BollingerPercentB
    """
    
    params = (
        ('indicators', {
            'VolumeDelta': {
                'class': VolumeDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeDelta'>
            },
            'BollingerPercentB': {
                'class': BollingerPercentB,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerPercentB'>
            }
        }),
        ('weights', {
            'VolumeDelta': 1.0,
            'BollingerPercentB': 1.0
        })
    )
