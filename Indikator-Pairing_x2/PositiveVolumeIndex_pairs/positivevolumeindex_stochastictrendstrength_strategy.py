import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PositiveVolumeIndex_StochasticTrendStrength_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PositiveVolumeIndex und StochasticTrendStrength
    """
    
    params = (
        ('indicators', {
            'PositiveVolumeIndex': {
                'class': PositiveVolumeIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PositiveVolumeIndex'>
            },
            'StochasticTrendStrength': {
                'class': StochasticTrendStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticTrendStrength'>
            }
        }),
        ('weights', {
            'PositiveVolumeIndex': 1.0,
            'StochasticTrendStrength': 1.0
        })
    )
