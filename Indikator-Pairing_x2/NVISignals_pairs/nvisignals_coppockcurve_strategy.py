import backtrader as bt
from ..base_strategy import FlexibleStrategy

class NVISignals_CoppockCurve_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von NVISignals und CoppockCurve
    """
    
    params = (
        ('indicators', {
            'NVISignals': {
                'class': NVISignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_NVISignals'>
            },
            'CoppockCurve': {
                'class': CoppockCurve,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CoppockCurve'>
            }
        }),
        ('weights', {
            'NVISignals': 1.0,
            'CoppockCurve': 1.0
        })
    )
