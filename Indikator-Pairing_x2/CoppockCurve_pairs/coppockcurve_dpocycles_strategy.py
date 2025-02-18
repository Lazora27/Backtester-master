import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CoppockCurve_DPOCycles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CoppockCurve und DPOCycles
    """
    
    params = (
        ('indicators', {
            'CoppockCurve': {
                'class': CoppockCurve,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CoppockCurve'>
            },
            'DPOCycles': {
                'class': DPOCycles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DPOCycles'>
            }
        }),
        ('weights', {
            'CoppockCurve': 1.0,
            'DPOCycles': 1.0
        })
    )
