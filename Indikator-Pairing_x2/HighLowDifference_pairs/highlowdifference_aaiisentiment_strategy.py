import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HighLowDifference_AAIISentiment_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HighLowDifference und AAIISentiment
    """
    
    params = (
        ('indicators', {
            'HighLowDifference': {
                'class': HighLowDifference,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HighLowDifference'>
            },
            'AAIISentiment': {
                'class': AAIISentiment,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AAIISentiment'>
            }
        }),
        ('weights', {
            'HighLowDifference': 1.0,
            'AAIISentiment': 1.0
        })
    )
