import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BalanceMomentum_ExtensionProjections_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BalanceMomentum und ExtensionProjections
    """
    
    params = (
        ('indicators', {
            'BalanceMomentum': {
                'class': BalanceMomentum,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BalanceMomentum'>
            },
            'ExtensionProjections': {
                'class': ExtensionProjections,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ExtensionProjections'>
            }
        }),
        ('weights', {
            'BalanceMomentum': 1.0,
            'ExtensionProjections': 1.0
        })
    )
