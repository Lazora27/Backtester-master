import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AAIISentiment_HistoricalATR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AAIISentiment und HistoricalATR
    """
    
    params = (
        ('indicators', {
            'AAIISentiment': {
                'class': AAIISentiment,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AAIISentiment'>
            },
            'HistoricalATR': {
                'class': HistoricalATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HistoricalATR'>
            }
        }),
        ('weights', {
            'AAIISentiment': 1.0,
            'HistoricalATR': 1.0
        })
    )
