import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CoppockCurve_FlowOfFunds_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CoppockCurve und FlowOfFunds
    """
    
    params = (
        ('indicators', {
            'CoppockCurve': {
                'class': CoppockCurve,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CoppockCurve'>
            },
            'FlowOfFunds': {
                'class': FlowOfFunds,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FlowOfFunds'>
            }
        }),
        ('weights', {
            'CoppockCurve': 1.0,
            'FlowOfFunds': 1.0
        })
    )
