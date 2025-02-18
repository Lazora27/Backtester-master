import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticTrendStrength_VolumeProfile_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticTrendStrength und VolumeProfile
    """
    
    params = (
        ('indicators', {
            'StochasticTrendStrength': {
                'class': StochasticTrendStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticTrendStrength'>
            },
            'VolumeProfile': {
                'class': VolumeProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeProfile'>
            }
        }),
        ('weights', {
            'StochasticTrendStrength': 1.0,
            'VolumeProfile': 1.0
        })
    )
