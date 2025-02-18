import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticRSI_VolumeDelta_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticRSI und VolumeDelta
    """
    
    params = (
        ('indicators', {
            'StochasticRSI': {
                'class': StochasticRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticRSI'>
            },
            'VolumeDelta': {
                'class': VolumeDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeDelta'>
            }
        }),
        ('weights', {
            'StochasticRSI': 1.0,
            'VolumeDelta': 1.0
        })
    )
