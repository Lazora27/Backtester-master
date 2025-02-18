import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CVIRatio_MarketOrderFlow_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CVIRatio und MarketOrderFlow
    """
    
    params = (
        ('indicators', {
            'CVIRatio': {
                'class': CVIRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CVIRatio'>
            },
            'MarketOrderFlow': {
                'class': MarketOrderFlow,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketOrderFlow'>
            }
        }),
        ('weights', {
            'CVIRatio': 1.0,
            'MarketOrderFlow': 1.0
        })
    )
