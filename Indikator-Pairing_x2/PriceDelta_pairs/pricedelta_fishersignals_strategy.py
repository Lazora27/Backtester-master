import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PriceDelta_FisherSignals_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PriceDelta und FisherSignals
    """
    
    params = (
        ('indicators', {
            'PriceDelta': {
                'class': PriceDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceDelta'>
            },
            'FisherSignals': {
                'class': FisherSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FisherSignals'>
            }
        }),
        ('weights', {
            'PriceDelta': 1.0,
            'FisherSignals': 1.0
        })
    )
