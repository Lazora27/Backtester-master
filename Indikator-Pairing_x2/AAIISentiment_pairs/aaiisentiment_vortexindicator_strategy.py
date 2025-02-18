import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AAIISentiment_VortexIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AAIISentiment und VortexIndicator
    """
    
    params = (
        ('indicators', {
            'AAIISentiment': {
                'class': AAIISentiment,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AAIISentiment'>
            },
            'VortexIndicator': {
                'class': VortexIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VortexIndicator'>
            }
        }),
        ('weights', {
            'AAIISentiment': 1.0,
            'VortexIndicator': 1.0
        })
    )
