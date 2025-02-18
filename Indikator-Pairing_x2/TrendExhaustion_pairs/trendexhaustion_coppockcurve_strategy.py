import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TrendExhaustion_CoppockCurve_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TrendExhaustion und CoppockCurve
    """
    
    params = (
        ('indicators', {
            'TrendExhaustion': {
                'class': TrendExhaustion,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrendExhaustion'>
            },
            'CoppockCurve': {
                'class': CoppockCurve,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CoppockCurve'>
            }
        }),
        ('weights', {
            'TrendExhaustion': 1.0,
            'CoppockCurve': 1.0
        })
    )
