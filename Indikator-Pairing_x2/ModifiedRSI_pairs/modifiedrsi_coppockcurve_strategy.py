import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ModifiedRSI_CoppockCurve_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ModifiedRSI und CoppockCurve
    """
    
    params = (
        ('indicators', {
            'ModifiedRSI': {
                'class': ModifiedRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ModifiedRSI'>
            },
            'CoppockCurve': {
                'class': CoppockCurve,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CoppockCurve'>
            }
        }),
        ('weights', {
            'ModifiedRSI': 1.0,
            'CoppockCurve': 1.0
        })
    )
