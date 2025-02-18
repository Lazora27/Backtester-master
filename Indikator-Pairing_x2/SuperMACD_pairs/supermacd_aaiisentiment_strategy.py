import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SuperMACD_AAIISentiment_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SuperMACD und AAIISentiment
    """
    
    params = (
        ('indicators', {
            'SuperMACD': {
                'class': SuperMACD,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SuperMACD'>
            },
            'AAIISentiment': {
                'class': AAIISentiment,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AAIISentiment'>
            }
        }),
        ('weights', {
            'SuperMACD': 1.0,
            'AAIISentiment': 1.0
        })
    )
