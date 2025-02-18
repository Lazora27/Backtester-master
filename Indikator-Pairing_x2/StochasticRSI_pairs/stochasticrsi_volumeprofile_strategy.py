import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticRSI_VolumeProfile_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticRSI und VolumeProfile
    """
    
    params = (
        ('indicators', {
            'StochasticRSI': {
                'class': StochasticRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticRSI'>
            },
            'VolumeProfile': {
                'class': VolumeProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeProfile'>
            }
        }),
        ('weights', {
            'StochasticRSI': 1.0,
            'VolumeProfile': 1.0
        })
    )
