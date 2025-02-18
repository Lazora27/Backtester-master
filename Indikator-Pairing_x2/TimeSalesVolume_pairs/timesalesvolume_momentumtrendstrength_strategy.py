import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TimeSalesVolume_MomentumTrendStrength_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TimeSalesVolume und MomentumTrendStrength
    """
    
    params = (
        ('indicators', {
            'TimeSalesVolume': {
                'class': TimeSalesVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeSalesVolume'>
            },
            'MomentumTrendStrength': {
                'class': MomentumTrendStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MomentumTrendStrength'>
            }
        }),
        ('weights', {
            'TimeSalesVolume': 1.0,
            'MomentumTrendStrength': 1.0
        })
    )
