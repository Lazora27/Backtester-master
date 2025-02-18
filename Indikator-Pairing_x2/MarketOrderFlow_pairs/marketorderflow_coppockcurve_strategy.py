import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MarketOrderFlow_CoppockCurve_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MarketOrderFlow und CoppockCurve
    """
    
    params = (
        ('indicators', {
            'MarketOrderFlow': {
                'class': MarketOrderFlow,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketOrderFlow'>
            },
            'CoppockCurve': {
                'class': CoppockCurve,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CoppockCurve'>
            }
        }),
        ('weights', {
            'MarketOrderFlow': 1.0,
            'CoppockCurve': 1.0
        })
    )
