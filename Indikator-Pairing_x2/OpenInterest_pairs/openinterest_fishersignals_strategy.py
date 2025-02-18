import backtrader as bt
from ..base_strategy import FlexibleStrategy

class OpenInterest_FisherSignals_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von OpenInterest und FisherSignals
    """
    
    params = (
        ('indicators', {
            'OpenInterest': {
                'class': OpenInterest,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OpenInterest'>
            },
            'FisherSignals': {
                'class': FisherSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FisherSignals'>
            }
        }),
        ('weights', {
            'OpenInterest': 1.0,
            'FisherSignals': 1.0
        })
    )
