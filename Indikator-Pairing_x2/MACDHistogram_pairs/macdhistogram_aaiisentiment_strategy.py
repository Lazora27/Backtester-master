import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDHistogram_AAIISentiment_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDHistogram und AAIISentiment
    """
    
    params = (
        ('indicators', {
            'MACDHistogram': {
                'class': MACDHistogram,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDHistogram'>
            },
            'AAIISentiment': {
                'class': AAIISentiment,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AAIISentiment'>
            }
        }),
        ('weights', {
            'MACDHistogram': 1.0,
            'AAIISentiment': 1.0
        })
    )
