import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CoppockCurve_ParabolicTimePrice_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CoppockCurve und ParabolicTimePrice
    """
    
    params = (
        ('indicators', {
            'CoppockCurve': {
                'class': CoppockCurve,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CoppockCurve'>
            },
            'ParabolicTimePrice': {
                'class': ParabolicTimePrice,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ParabolicTimePrice'>
            }
        }),
        ('weights', {
            'CoppockCurve': 1.0,
            'ParabolicTimePrice': 1.0
        })
    )
