import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticTrendStrength_TimeSalesVolume_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticTrendStrength und TimeSalesVolume
    """
    
    params = (
        ('indicators', {
            'StochasticTrendStrength': {
                'class': StochasticTrendStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticTrendStrength'>
            },
            'TimeSalesVolume': {
                'class': TimeSalesVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeSalesVolume'>
            }
        }),
        ('weights', {
            'StochasticTrendStrength': 1.0,
            'TimeSalesVolume': 1.0
        })
    )
