import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BalanceMomentum_SeasonalStrength_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BalanceMomentum und SeasonalStrength
    """
    
    params = (
        ('indicators', {
            'BalanceMomentum': {
                'class': BalanceMomentum,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BalanceMomentum'>
            },
            'SeasonalStrength': {
                'class': SeasonalStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SeasonalStrength'>
            }
        }),
        ('weights', {
            'BalanceMomentum': 1.0,
            'SeasonalStrength': 1.0
        })
    )
