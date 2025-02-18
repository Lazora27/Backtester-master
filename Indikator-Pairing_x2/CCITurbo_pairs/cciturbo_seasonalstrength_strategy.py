import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CCITurbo_SeasonalStrength_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CCITurbo und SeasonalStrength
    """
    
    params = (
        ('indicators', {
            'CCITurbo': {
                'class': CCITurbo,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CCITurbo'>
            },
            'SeasonalStrength': {
                'class': SeasonalStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SeasonalStrength'>
            }
        }),
        ('weights', {
            'CCITurbo': 1.0,
            'SeasonalStrength': 1.0
        })
    )
