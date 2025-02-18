import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VolumeProfile_BollingerPercentB_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VolumeProfile und BollingerPercentB
    """
    
    params = (
        ('indicators', {
            'VolumeProfile': {
                'class': VolumeProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeProfile'>
            },
            'BollingerPercentB': {
                'class': BollingerPercentB,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerPercentB'>
            }
        }),
        ('weights', {
            'VolumeProfile': 1.0,
            'BollingerPercentB': 1.0
        })
    )
