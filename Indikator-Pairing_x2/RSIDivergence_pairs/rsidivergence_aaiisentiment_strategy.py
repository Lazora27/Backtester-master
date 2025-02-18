import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RSIDivergence_AAIISentiment_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RSIDivergence und AAIISentiment
    """
    
    params = (
        ('indicators', {
            'RSIDivergence': {
                'class': RSIDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RSIDivergence'>
            },
            'AAIISentiment': {
                'class': AAIISentiment,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AAIISentiment'>
            }
        }),
        ('weights', {
            'RSIDivergence': 1.0,
            'AAIISentiment': 1.0
        })
    )
