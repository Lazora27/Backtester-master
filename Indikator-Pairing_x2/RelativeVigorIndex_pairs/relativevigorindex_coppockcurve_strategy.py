import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RelativeVigorIndex_CoppockCurve_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RelativeVigorIndex und CoppockCurve
    """
    
    params = (
        ('indicators', {
            'RelativeVigorIndex': {
                'class': RelativeVigorIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RelativeVigorIndex'>
            },
            'CoppockCurve': {
                'class': CoppockCurve,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CoppockCurve'>
            }
        }),
        ('weights', {
            'RelativeVigorIndex': 1.0,
            'CoppockCurve': 1.0
        })
    )
