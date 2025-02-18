import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TickVolume_SeasonalStrength_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TickVolume und SeasonalStrength
    """
    
    params = (
        ('indicators', {
            'TickVolume': {
                'class': TickVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickVolume'>
            },
            'SeasonalStrength': {
                'class': SeasonalStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SeasonalStrength'>
            }
        }),
        ('weights', {
            'TickVolume': 1.0,
            'SeasonalStrength': 1.0
        })
    )
