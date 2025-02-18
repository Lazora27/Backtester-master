import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VWAPBands_CoppockCurve_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VWAPBands und CoppockCurve
    """
    
    params = (
        ('indicators', {
            'VWAPBands': {
                'class': VWAPBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VWAPBands'>
            },
            'CoppockCurve': {
                'class': CoppockCurve,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CoppockCurve'>
            }
        }),
        ('weights', {
            'VWAPBands': 1.0,
            'CoppockCurve': 1.0
        })
    )
