import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BollingerBandSqueeze_BollingerPercentB_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BollingerBandSqueeze und BollingerPercentB
    """
    
    params = (
        ('indicators', {
            'BollingerBandSqueeze': {
                'class': BollingerBandSqueeze,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBandSqueeze'>
            },
            'BollingerPercentB': {
                'class': BollingerPercentB,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerPercentB'>
            }
        }),
        ('weights', {
            'BollingerBandSqueeze': 1.0,
            'BollingerPercentB': 1.0
        })
    )
