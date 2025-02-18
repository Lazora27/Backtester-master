import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HighLowIndex_AAIISentiment_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HighLowIndex und AAIISentiment
    """
    
    params = (
        ('indicators', {
            'HighLowIndex': {
                'class': HighLowIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HighLowIndex'>
            },
            'AAIISentiment': {
                'class': AAIISentiment,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AAIISentiment'>
            }
        }),
        ('weights', {
            'HighLowIndex': 1.0,
            'AAIISentiment': 1.0
        })
    )
