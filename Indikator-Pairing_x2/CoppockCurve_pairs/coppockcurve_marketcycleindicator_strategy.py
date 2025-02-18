import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CoppockCurve_MarketCycleIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CoppockCurve und MarketCycleIndicator
    """
    
    params = (
        ('indicators', {
            'CoppockCurve': {
                'class': CoppockCurve,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CoppockCurve'>
            },
            'MarketCycleIndicator': {
                'class': MarketCycleIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketCycleIndicator'>
            }
        }),
        ('weights', {
            'CoppockCurve': 1.0,
            'MarketCycleIndicator': 1.0
        })
    )
