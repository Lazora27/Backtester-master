import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AAIISentiment_EhlersFisherTransform_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AAIISentiment und EhlersFisherTransform
    """
    
    params = (
        ('indicators', {
            'AAIISentiment': {
                'class': AAIISentiment,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AAIISentiment'>
            },
            'EhlersFisherTransform': {
                'class': EhlersFisherTransform,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EhlersFisherTransform'>
            }
        }),
        ('weights', {
            'AAIISentiment': 1.0,
            'EhlersFisherTransform': 1.0
        })
    )
