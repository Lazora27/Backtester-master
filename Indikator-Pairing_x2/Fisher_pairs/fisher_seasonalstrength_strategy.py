import backtrader as bt
from ..base_strategy import FlexibleStrategy

class Fisher_SeasonalStrength_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von Fisher und SeasonalStrength
    """
    
    params = (
        ('indicators', {
            'Fisher': {
                'class': Fisher,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_Fisher'>
            },
            'SeasonalStrength': {
                'class': SeasonalStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SeasonalStrength'>
            }
        }),
        ('weights', {
            'Fisher': 1.0,
            'SeasonalStrength': 1.0
        })
    )
