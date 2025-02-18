import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticDivergence_VolumeProfile_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticDivergence und VolumeProfile
    """
    
    params = (
        ('indicators', {
            'StochasticDivergence': {
                'class': StochasticDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticDivergence'>
            },
            'VolumeProfile': {
                'class': VolumeProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeProfile'>
            }
        }),
        ('weights', {
            'StochasticDivergence': 1.0,
            'VolumeProfile': 1.0
        })
    )
