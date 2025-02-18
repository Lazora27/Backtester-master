import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticDivergence_VolumeFlowIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticDivergence und VolumeFlowIndicator
    """
    
    params = (
        ('indicators', {
            'StochasticDivergence': {
                'class': StochasticDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticDivergence'>
            },
            'VolumeFlowIndicator': {
                'class': VolumeFlowIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeFlowIndicator'>
            }
        }),
        ('weights', {
            'StochasticDivergence': 1.0,
            'VolumeFlowIndicator': 1.0
        })
    )
