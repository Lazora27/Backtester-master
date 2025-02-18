import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CoppockCurve_TimeCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CoppockCurve und TimeCycle
    """
    
    params = (
        ('indicators', {
            'CoppockCurve': {
                'class': CoppockCurve,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CoppockCurve'>
            },
            'TimeCycle': {
                'class': TimeCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeCycle'>
            }
        }),
        ('weights', {
            'CoppockCurve': 1.0,
            'TimeCycle': 1.0
        })
    )
