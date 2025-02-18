import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CoppockCurve_BuyingPressure_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CoppockCurve und BuyingPressure
    """
    
    params = (
        ('indicators', {
            'CoppockCurve': {
                'class': CoppockCurve,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CoppockCurve'>
            },
            'BuyingPressure': {
                'class': BuyingPressure,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BuyingPressure'>
            }
        }),
        ('weights', {
            'CoppockCurve': 1.0,
            'BuyingPressure': 1.0
        })
    )
