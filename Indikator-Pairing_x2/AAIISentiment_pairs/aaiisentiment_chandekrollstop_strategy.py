import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AAIISentiment_ChandeKrollStop_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AAIISentiment und ChandeKrollStop
    """
    
    params = (
        ('indicators', {
            'AAIISentiment': {
                'class': AAIISentiment,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AAIISentiment'>
            },
            'ChandeKrollStop': {
                'class': ChandeKrollStop,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChandeKrollStop'>
            }
        }),
        ('weights', {
            'AAIISentiment': 1.0,
            'ChandeKrollStop': 1.0
        })
    )
