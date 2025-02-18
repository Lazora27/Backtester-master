import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PutCallRatio_AAIISentiment_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PutCallRatio und AAIISentiment
    """
    
    params = (
        ('indicators', {
            'PutCallRatio': {
                'class': PutCallRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PutCallRatio1'>
            },
            'AAIISentiment': {
                'class': AAIISentiment,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AAIISentiment'>
            }
        }),
        ('weights', {
            'PutCallRatio': 1.0,
            'AAIISentiment': 1.0
        })
    )
