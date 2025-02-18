import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CoppockCurve_DemandIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CoppockCurve und DemandIndex
    """
    
    params = (
        ('indicators', {
            'CoppockCurve': {
                'class': CoppockCurve,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CoppockCurve'>
            },
            'DemandIndex': {
                'class': DemandIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DemandIndex'>
            }
        }),
        ('weights', {
            'CoppockCurve': 1.0,
            'DemandIndex': 1.0
        })
    )
