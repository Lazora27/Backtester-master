import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TickIndex_AAIISentiment_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TickIndex und AAIISentiment
    """
    
    params = (
        ('indicators', {
            'TickIndex': {
                'class': TickIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickIndex'>
            },
            'AAIISentiment': {
                'class': AAIISentiment,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AAIISentiment'>
            }
        }),
        ('weights', {
            'TickIndex': 1.0,
            'AAIISentiment': 1.0
        })
    )
