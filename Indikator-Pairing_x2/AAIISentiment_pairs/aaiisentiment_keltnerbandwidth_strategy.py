import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AAIISentiment_KeltnerBandWidth_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AAIISentiment und KeltnerBandWidth
    """
    
    params = (
        ('indicators', {
            'AAIISentiment': {
                'class': AAIISentiment,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AAIISentiment'>
            },
            'KeltnerBandWidth': {
                'class': KeltnerBandWidth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KeltnerBandWidth'>
            }
        }),
        ('weights', {
            'AAIISentiment': 1.0,
            'KeltnerBandWidth': 1.0
        })
    )
