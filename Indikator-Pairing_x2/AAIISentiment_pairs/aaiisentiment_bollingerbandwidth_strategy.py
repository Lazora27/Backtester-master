import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AAIISentiment_BollingerBandWidth_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AAIISentiment und BollingerBandWidth
    """
    
    params = (
        ('indicators', {
            'AAIISentiment': {
                'class': AAIISentiment,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AAIISentiment'>
            },
            'BollingerBandWidth': {
                'class': BollingerBandWidth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBandWidth'>
            }
        }),
        ('weights', {
            'AAIISentiment': 1.0,
            'BollingerBandWidth': 1.0
        })
    )
