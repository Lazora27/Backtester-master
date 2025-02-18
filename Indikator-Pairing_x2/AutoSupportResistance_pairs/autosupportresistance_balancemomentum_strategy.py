import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AutoSupportResistance_BalanceMomentum_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AutoSupportResistance und BalanceMomentum
    """
    
    params = (
        ('indicators', {
            'AutoSupportResistance': {
                'class': AutoSupportResistance,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AutoSupportResistance'>
            },
            'BalanceMomentum': {
                'class': BalanceMomentum,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BalanceMomentum'>
            }
        }),
        ('weights', {
            'AutoSupportResistance': 1.0,
            'BalanceMomentum': 1.0
        })
    )
