import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BollingerPercentB_VolumeTrendIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BollingerPercentB und VolumeTrendIndicator
    """
    
    params = (
        ('indicators', {
            'BollingerPercentB': {
                'class': BollingerPercentB,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerPercentB'>
            },
            'VolumeTrendIndicator': {
                'class': VolumeTrendIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeTrendIndicator'>
            }
        }),
        ('weights', {
            'BollingerPercentB': 1.0,
            'VolumeTrendIndicator': 1.0
        })
    )
