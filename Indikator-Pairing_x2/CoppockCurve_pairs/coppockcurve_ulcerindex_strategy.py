import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CoppockCurve_UlcerIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CoppockCurve und UlcerIndex
    """
    
    params = (
        ('indicators', {
            'CoppockCurve': {
                'class': CoppockCurve,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CoppockCurve'>
            },
            'UlcerIndex': {
                'class': UlcerIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_UlcerIndex'>
            }
        }),
        ('weights', {
            'CoppockCurve': 1.0,
            'UlcerIndex': 1.0
        })
    )
