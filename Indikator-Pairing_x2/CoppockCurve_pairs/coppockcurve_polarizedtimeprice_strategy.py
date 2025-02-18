import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CoppockCurve_PolarizedTimePrice_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CoppockCurve und PolarizedTimePrice
    """
    
    params = (
        ('indicators', {
            'CoppockCurve': {
                'class': CoppockCurve,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CoppockCurve'>
            },
            'PolarizedTimePrice': {
                'class': PolarizedTimePrice,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PolarizedTimePrice'>
            }
        }),
        ('weights', {
            'CoppockCurve': 1.0,
            'PolarizedTimePrice': 1.0
        })
    )
