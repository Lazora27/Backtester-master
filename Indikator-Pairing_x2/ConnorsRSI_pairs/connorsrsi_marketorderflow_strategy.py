import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ConnorsRSI_MarketOrderFlow_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ConnorsRSI und MarketOrderFlow
    """
    
    params = (
        ('indicators', {
            'ConnorsRSI': {
                'class': ConnorsRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ConnorsRSI'>
            },
            'MarketOrderFlow': {
                'class': MarketOrderFlow,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketOrderFlow'>
            }
        }),
        ('weights', {
            'ConnorsRSI': 1.0,
            'MarketOrderFlow': 1.0
        })
    )
