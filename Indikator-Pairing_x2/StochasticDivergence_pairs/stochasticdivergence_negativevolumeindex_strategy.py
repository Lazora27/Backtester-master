import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticDivergence_NegativeVolumeIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticDivergence und NegativeVolumeIndex
    """
    
    params = (
        ('indicators', {
            'StochasticDivergence': {
                'class': StochasticDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticDivergence'>
            },
            'NegativeVolumeIndex': {
                'class': NegativeVolumeIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_NegativeVolumeIndex'>
            }
        }),
        ('weights', {
            'StochasticDivergence': 1.0,
            'NegativeVolumeIndex': 1.0
        })
    )
