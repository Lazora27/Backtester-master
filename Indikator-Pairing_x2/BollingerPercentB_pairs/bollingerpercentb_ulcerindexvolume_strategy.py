import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BollingerPercentB_UlcerIndexVolume_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BollingerPercentB und UlcerIndexVolume
    """
    
    params = (
        ('indicators', {
            'BollingerPercentB': {
                'class': BollingerPercentB,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerPercentB'>
            },
            'UlcerIndexVolume': {
                'class': UlcerIndexVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_UlcerIndexVolume'>
            }
        }),
        ('weights', {
            'BollingerPercentB': 1.0,
            'UlcerIndexVolume': 1.0
        })
    )
