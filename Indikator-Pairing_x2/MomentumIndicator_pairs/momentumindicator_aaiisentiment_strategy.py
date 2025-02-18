import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MomentumIndicator_AAIISentiment_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MomentumIndicator und AAIISentiment
    """
    
    params = (
        ('indicators', {
            'MomentumIndicator': {
                'class': MomentumIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MomentumIndicator'>
            },
            'AAIISentiment': {
                'class': AAIISentiment,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AAIISentiment'>
            }
        }),
        ('weights', {
            'MomentumIndicator': 1.0,
            'AAIISentiment': 1.0
        })
    )
