import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BalanceMomentum_AAIISentiment_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BalanceMomentum und AAIISentiment
    """
    
    params = (
        ('indicators', {
            'BalanceMomentum': {
                'class': BalanceMomentum,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BalanceMomentum'>
            },
            'AAIISentiment': {
                'class': AAIISentiment,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AAIISentiment'>
            }
        }),
        ('weights', {
            'BalanceMomentum': 1.0,
            'AAIISentiment': 1.0
        })
    )
