import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WilliamsR_AAIISentiment_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WilliamsR und AAIISentiment
    """
    
    params = (
        ('indicators', {
            'WilliamsR': {
                'class': WilliamsR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WilliamsR1'>
            },
            'AAIISentiment': {
                'class': AAIISentiment,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AAIISentiment'>
            }
        }),
        ('weights', {
            'WilliamsR': 1.0,
            'AAIISentiment': 1.0
        })
    )
