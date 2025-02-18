import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TimeSalesVolume_SeasonalStrength_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TimeSalesVolume und SeasonalStrength
    """
    
    params = (
        ('indicators', {
            'TimeSalesVolume': {
                'class': TimeSalesVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeSalesVolume'>
            },
            'SeasonalStrength': {
                'class': SeasonalStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SeasonalStrength'>
            }
        }),
        ('weights', {
            'TimeSalesVolume': 1.0,
            'SeasonalStrength': 1.0
        })
    )
