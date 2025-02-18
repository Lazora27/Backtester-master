import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AAIISentiment_UlcerIndexVolume_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AAIISentiment und UlcerIndexVolume
    """
    
    params = (
        ('indicators', {
            'AAIISentiment': {
                'class': AAIISentiment,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AAIISentiment'>
            },
            'UlcerIndexVolume': {
                'class': UlcerIndexVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_UlcerIndexVolume'>
            }
        }),
        ('weights', {
            'AAIISentiment': 1.0,
            'UlcerIndexVolume': 1.0
        })
    )
