import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DPOCycles_PhaseDivergence_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DPOCycles und PhaseDivergence
    """
    
    params = (
        ('indicators', {
            'DPOCycles': {
                'class': DPOCycles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DPOCycles'>
            },
            'PhaseDivergence': {
                'class': PhaseDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PhaseDivergence'>
            }
        }),
        ('weights', {
            'DPOCycles': 1.0,
            'PhaseDivergence': 1.0
        })
    )
