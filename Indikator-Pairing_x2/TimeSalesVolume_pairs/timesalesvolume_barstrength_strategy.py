import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TimeSalesVolume_BarStrength_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TimeSalesVolume und BarStrength
    """
    
    params = (
        ('indicators', {
            'TimeSalesVolume': {
                'class': TimeSalesVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeSalesVolume'>
            },
            'BarStrength': {
                'class': BarStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BarStrength'>
            }
        }),
        ('weights', {
            'TimeSalesVolume': 1.0,
            'BarStrength': 1.0
        })
    )
