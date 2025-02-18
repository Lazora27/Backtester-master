import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AccelerationBands_SeasonalStrength_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AccelerationBands und SeasonalStrength
    """
    
    params = (
        ('indicators', {
            'AccelerationBands': {
                'class': AccelerationBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AccelerationBands'>
            },
            'SeasonalStrength': {
                'class': SeasonalStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SeasonalStrength'>
            }
        }),
        ('weights', {
            'AccelerationBands': 1.0,
            'SeasonalStrength': 1.0
        })
    )
