import backtrader as bt
from ..base_strategy import FlexibleStrategy

class KDJIndicator_AAIISentiment_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von KDJIndicator und AAIISentiment
    """
    
    params = (
        ('indicators', {
            'KDJIndicator': {
                'class': KDJIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KDJIndicator'>
            },
            'AAIISentiment': {
                'class': AAIISentiment,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AAIISentiment'>
            }
        }),
        ('weights', {
            'KDJIndicator': 1.0,
            'AAIISentiment': 1.0
        })
    )
