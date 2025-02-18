import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AAIISentiment_IchimokuCloud_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AAIISentiment und IchimokuCloud
    """
    
    params = (
        ('indicators', {
            'AAIISentiment': {
                'class': AAIISentiment,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AAIISentiment'>
            },
            'IchimokuCloud': {
                'class': IchimokuCloud,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_IchimokuCloud'>
            }
        }),
        ('weights', {
            'AAIISentiment': 1.0,
            'IchimokuCloud': 1.0
        })
    )
