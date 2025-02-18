import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MarketBalance_FisherSignals_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MarketBalance und FisherSignals
    """
    
    params = (
        ('indicators', {
            'MarketBalance': {
                'class': MarketBalance,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketBalance'>
            },
            'FisherSignals': {
                'class': FisherSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FisherSignals'>
            }
        }),
        ('weights', {
            'MarketBalance': 1.0,
            'FisherSignals': 1.0
        })
    )
