import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticMomentumIndex_VolumeProfile_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticMomentumIndex und VolumeProfile
    """
    
    params = (
        ('indicators', {
            'StochasticMomentumIndex': {
                'class': StochasticMomentumIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticMomentumIndex'>
            },
            'VolumeProfile': {
                'class': VolumeProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeProfile'>
            }
        }),
        ('weights', {
            'StochasticMomentumIndex': 1.0,
            'VolumeProfile': 1.0
        })
    )
