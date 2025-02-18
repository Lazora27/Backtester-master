import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CoppockCurve_MarketBalance_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CoppockCurve und MarketBalance
    """
    
    params = (
        ('indicators', {
            'CoppockCurve': {
                'class': CoppockCurve,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CoppockCurve'>
            },
            'MarketBalance': {
                'class': MarketBalance,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketBalance'>
            }
        }),
        ('weights', {
            'CoppockCurve': 1.0,
            'MarketBalance': 1.0
        })
    )
