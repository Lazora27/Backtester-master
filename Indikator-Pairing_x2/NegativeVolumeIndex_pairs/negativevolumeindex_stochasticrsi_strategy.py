import backtrader as bt
from ..base_strategy import FlexibleStrategy

class NegativeVolumeIndex_StochasticRSI_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von NegativeVolumeIndex und StochasticRSI
    """
    
    params = (
        ('indicators', {
            'NegativeVolumeIndex': {
                'class': NegativeVolumeIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_NegativeVolumeIndex'>
            },
            'StochasticRSI': {
                'class': StochasticRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticRSI'>
            }
        }),
        ('weights', {
            'NegativeVolumeIndex': 1.0,
            'StochasticRSI': 1.0
        })
    )
