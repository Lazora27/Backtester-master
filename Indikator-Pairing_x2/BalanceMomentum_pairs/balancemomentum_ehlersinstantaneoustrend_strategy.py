import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BalanceMomentum_EhlersInstantaneousTrend_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BalanceMomentum und EhlersInstantaneousTrend
    """
    
    params = (
        ('indicators', {
            'BalanceMomentum': {
                'class': BalanceMomentum,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BalanceMomentum'>
            },
            'EhlersInstantaneousTrend': {
                'class': EhlersInstantaneousTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EhlersInstantaneousTrend'>
            }
        }),
        ('weights', {
            'BalanceMomentum': 1.0,
            'EhlersInstantaneousTrend': 1.0
        })
    )
