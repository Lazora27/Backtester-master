import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AverageLogRange_SeasonalStrength_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AverageLogRange und SeasonalStrength
    """
    
    params = (
        ('indicators', {
            'AverageLogRange': {
                'class': AverageLogRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageLogRange'>
            },
            'SeasonalStrength': {
                'class': SeasonalStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SeasonalStrength'>
            }
        }),
        ('weights', {
            'AverageLogRange': 1.0,
            'SeasonalStrength': 1.0
        })
    )
