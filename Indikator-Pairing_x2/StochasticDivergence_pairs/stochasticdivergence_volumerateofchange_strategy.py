import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticDivergence_VolumeRateOfChange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticDivergence und VolumeRateOfChange
    """
    
    params = (
        ('indicators', {
            'StochasticDivergence': {
                'class': StochasticDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticDivergence'>
            },
            'VolumeRateOfChange': {
                'class': VolumeRateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeRateOfChange'>
            }
        }),
        ('weights', {
            'StochasticDivergence': 1.0,
            'VolumeRateOfChange': 1.0
        })
    )
