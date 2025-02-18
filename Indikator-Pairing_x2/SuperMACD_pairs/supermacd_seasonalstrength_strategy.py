import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SuperMACD_SeasonalStrength_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SuperMACD und SeasonalStrength
    """
    
    params = (
        ('indicators', {
            'SuperMACD': {
                'class': SuperMACD,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SuperMACD'>
            },
            'SeasonalStrength': {
                'class': SeasonalStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SeasonalStrength'>
            }
        }),
        ('weights', {
            'SuperMACD': 1.0,
            'SeasonalStrength': 1.0
        })
    )
