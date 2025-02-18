import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ParabolicSAR_DPOCycles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ParabolicSAR und DPOCycles
    """
    
    params = (
        ('indicators', {
            'ParabolicSAR': {
                'class': ParabolicSAR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ParabolicSAR'>
            },
            'DPOCycles': {
                'class': DPOCycles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DPOCycles'>
            }
        }),
        ('weights', {
            'ParabolicSAR': 1.0,
            'DPOCycles': 1.0
        })
    )
