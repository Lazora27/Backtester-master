import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PriceDelta_CoppockCurve_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PriceDelta und CoppockCurve
    """
    
    params = (
        ('indicators', {
            'PriceDelta': {
                'class': PriceDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceDelta'>
            },
            'CoppockCurve': {
                'class': CoppockCurve,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CoppockCurve'>
            }
        }),
        ('weights', {
            'PriceDelta': 1.0,
            'CoppockCurve': 1.0
        })
    )
