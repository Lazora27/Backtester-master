import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticTrendStrength_VolumeFlowIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticTrendStrength und VolumeFlowIndicator
    """
    
    params = (
        ('indicators', {
            'StochasticTrendStrength': {
                'class': StochasticTrendStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticTrendStrength'>
            },
            'VolumeFlowIndicator': {
                'class': VolumeFlowIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeFlowIndicator'>
            }
        }),
        ('weights', {
            'StochasticTrendStrength': 1.0,
            'VolumeFlowIndicator': 1.0
        })
    )
