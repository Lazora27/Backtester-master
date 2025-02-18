import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticDivergence_VolumeTrendIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticDivergence und VolumeTrendIndicator
    """
    
    params = (
        ('indicators', {
            'StochasticDivergence': {
                'class': StochasticDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticDivergence'>
            },
            'VolumeTrendIndicator': {
                'class': VolumeTrendIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeTrendIndicator'>
            }
        }),
        ('weights', {
            'StochasticDivergence': 1.0,
            'VolumeTrendIndicator': 1.0
        })
    )
