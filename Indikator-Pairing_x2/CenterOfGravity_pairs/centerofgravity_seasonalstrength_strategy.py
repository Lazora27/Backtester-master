import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CenterOfGravity_SeasonalStrength_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CenterOfGravity und SeasonalStrength
    """
    
    params = (
        ('indicators', {
            'CenterOfGravity': {
                'class': CenterOfGravity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CenterOfGravity'>
            },
            'SeasonalStrength': {
                'class': SeasonalStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SeasonalStrength'>
            }
        }),
        ('weights', {
            'CenterOfGravity': 1.0,
            'SeasonalStrength': 1.0
        })
    )
