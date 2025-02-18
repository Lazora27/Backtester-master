import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BarStrength_SeasonalStrength_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BarStrength und SeasonalStrength
    """
    
    params = (
        ('indicators', {
            'BarStrength': {
                'class': BarStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BarStrength'>
            },
            'SeasonalStrength': {
                'class': SeasonalStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SeasonalStrength'>
            }
        }),
        ('weights', {
            'BarStrength': 1.0,
            'SeasonalStrength': 1.0
        })
    )
