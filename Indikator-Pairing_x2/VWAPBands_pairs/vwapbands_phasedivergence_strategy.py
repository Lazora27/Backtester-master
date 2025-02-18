import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VWAPBands_PhaseDivergence_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VWAPBands und PhaseDivergence
    """
    
    params = (
        ('indicators', {
            'VWAPBands': {
                'class': VWAPBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VWAPBands'>
            },
            'PhaseDivergence': {
                'class': PhaseDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PhaseDivergence'>
            }
        }),
        ('weights', {
            'VWAPBands': 1.0,
            'PhaseDivergence': 1.0
        })
    )
