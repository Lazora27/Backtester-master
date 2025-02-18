import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MarketOrderFlow_ProjectionBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MarketOrderFlow und ProjectionBands
    """
    
    params = (
        ('indicators', {
            'MarketOrderFlow': {
                'class': MarketOrderFlow,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketOrderFlow'>
            },
            'ProjectionBands': {
                'class': ProjectionBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ProjectionBands'>
            }
        }),
        ('weights', {
            'MarketOrderFlow': 1.0,
            'ProjectionBands': 1.0
        })
    )
