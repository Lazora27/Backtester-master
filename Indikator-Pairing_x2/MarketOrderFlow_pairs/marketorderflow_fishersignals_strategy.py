import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MarketOrderFlow_FisherSignals_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MarketOrderFlow und FisherSignals
    """
    
    params = (
        ('indicators', {
            'MarketOrderFlow': {
                'class': MarketOrderFlow,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketOrderFlow'>
            },
            'FisherSignals': {
                'class': FisherSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FisherSignals'>
            }
        }),
        ('weights', {
            'MarketOrderFlow': 1.0,
            'FisherSignals': 1.0
        })
    )
