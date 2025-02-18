import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AdvanceDeclineLine_DPOCycles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AdvanceDeclineLine und DPOCycles
    """
    
    params = (
        ('indicators', {
            'AdvanceDeclineLine': {
                'class': AdvanceDeclineLine,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdvanceDeclineLine'>
            },
            'DPOCycles': {
                'class': DPOCycles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DPOCycles'>
            }
        }),
        ('weights', {
            'AdvanceDeclineLine': 1.0,
            'DPOCycles': 1.0
        })
    )
