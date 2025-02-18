import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FisherTransform_AAIISentiment_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FisherTransform und AAIISentiment
    """
    
    params = (
        ('indicators', {
            'FisherTransform': {
                'class': FisherTransform,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FisherTransform'>
            },
            'AAIISentiment': {
                'class': AAIISentiment,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AAIISentiment'>
            }
        }),
        ('weights', {
            'FisherTransform': 1.0,
            'AAIISentiment': 1.0
        })
    )
