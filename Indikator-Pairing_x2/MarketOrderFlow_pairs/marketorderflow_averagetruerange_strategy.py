import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MarketOrderFlow_AverageTrueRange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MarketOrderFlow und AverageTrueRange
    """
    
    params = (
        ('indicators', {
            'MarketOrderFlow': {
                'class': MarketOrderFlow,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketOrderFlow'>
            },
            'AverageTrueRange': {
                'class': AverageTrueRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageTrueRange1'>
            }
        }),
        ('weights', {
            'MarketOrderFlow': 1.0,
            'AverageTrueRange': 1.0
        })
    )
