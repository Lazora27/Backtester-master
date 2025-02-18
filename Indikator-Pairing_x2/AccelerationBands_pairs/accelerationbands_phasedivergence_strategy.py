import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AccelerationBands_PhaseDivergence_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AccelerationBands und PhaseDivergence
    """
    
    params = (
        ('indicators', {
            'AccelerationBands': {
                'class': AccelerationBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AccelerationBands'>
            },
            'PhaseDivergence': {
                'class': PhaseDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PhaseDivergence'>
            }
        }),
        ('weights', {
            'AccelerationBands': 1.0,
            'PhaseDivergence': 1.0
        })
    )
