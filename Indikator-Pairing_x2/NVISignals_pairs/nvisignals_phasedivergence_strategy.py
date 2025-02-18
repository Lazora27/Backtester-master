import backtrader as bt
from ..base_strategy import FlexibleStrategy

class NVISignals_PhaseDivergence_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von NVISignals und PhaseDivergence
    """
    
    params = (
        ('indicators', {
            'NVISignals': {
                'class': NVISignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_NVISignals'>
            },
            'PhaseDivergence': {
                'class': PhaseDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PhaseDivergence'>
            }
        }),
        ('weights', {
            'NVISignals': 1.0,
            'PhaseDivergence': 1.0
        })
    )
