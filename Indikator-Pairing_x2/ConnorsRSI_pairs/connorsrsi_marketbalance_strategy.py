import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ConnorsRSI_MarketBalance_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ConnorsRSI und MarketBalance
    """
    
    params = (
        ('indicators', {
            'ConnorsRSI': {
                'class': ConnorsRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ConnorsRSI'>
            },
            'MarketBalance': {
                'class': MarketBalance,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketBalance'>
            }
        }),
        ('weights', {
            'ConnorsRSI': 1.0,
            'MarketBalance': 1.0
        })
    )
