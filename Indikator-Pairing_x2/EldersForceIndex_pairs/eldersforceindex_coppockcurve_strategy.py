import backtrader as bt
from ..base_strategy import FlexibleStrategy

class EldersForceIndex_CoppockCurve_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von EldersForceIndex und CoppockCurve
    """
    
    params = (
        ('indicators', {
            'EldersForceIndex': {
                'class': EldersForceIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EldersForceIndex'>
            },
            'CoppockCurve': {
                'class': CoppockCurve,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CoppockCurve'>
            }
        }),
        ('weights', {
            'EldersForceIndex': 1.0,
            'CoppockCurve': 1.0
        })
    )
