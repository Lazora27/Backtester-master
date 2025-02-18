import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CVIRatio_PhaseDivergence_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CVIRatio und PhaseDivergence
    """
    
    params = (
        ('indicators', {
            'CVIRatio': {
                'class': CVIRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CVIRatio'>
            },
            'PhaseDivergence': {
                'class': PhaseDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PhaseDivergence'>
            }
        }),
        ('weights', {
            'CVIRatio': 1.0,
            'PhaseDivergence': 1.0
        })
    )
