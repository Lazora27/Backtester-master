import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticDivergence_PositiveVolumeIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticDivergence und PositiveVolumeIndex
    """
    
    params = (
        ('indicators', {
            'StochasticDivergence': {
                'class': StochasticDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticDivergence'>
            },
            'PositiveVolumeIndex': {
                'class': PositiveVolumeIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PositiveVolumeIndex'>
            }
        }),
        ('weights', {
            'StochasticDivergence': 1.0,
            'PositiveVolumeIndex': 1.0
        })
    )
