import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AAIISentiment_EhlersDecycler_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AAIISentiment und EhlersDecycler
    """
    
    params = (
        ('indicators', {
            'AAIISentiment': {
                'class': AAIISentiment,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AAIISentiment'>
            },
            'EhlersDecycler': {
                'class': EhlersDecycler,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EhlersDecycler'>
            }
        }),
        ('weights', {
            'AAIISentiment': 1.0,
            'EhlersDecycler': 1.0
        })
    )
