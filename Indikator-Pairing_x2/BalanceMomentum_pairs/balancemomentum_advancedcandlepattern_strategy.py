import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BalanceMomentum_AdvancedCandlePattern_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BalanceMomentum und AdvancedCandlePattern
    """
    
    params = (
        ('indicators', {
            'BalanceMomentum': {
                'class': BalanceMomentum,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BalanceMomentum'>
            },
            'AdvancedCandlePattern': {
                'class': AdvancedCandlePattern,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdvancedCandlePattern'>
            }
        }),
        ('weights', {
            'BalanceMomentum': 1.0,
            'AdvancedCandlePattern': 1.0
        })
    )
