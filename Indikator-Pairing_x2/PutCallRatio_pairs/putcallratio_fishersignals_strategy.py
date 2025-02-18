import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PutCallRatio_FisherSignals_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PutCallRatio und FisherSignals
    """
    
    params = (
        ('indicators', {
            'PutCallRatio': {
                'class': PutCallRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PutCallRatio1'>
            },
            'FisherSignals': {
                'class': FisherSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FisherSignals'>
            }
        }),
        ('weights', {
            'PutCallRatio': 1.0,
            'FisherSignals': 1.0
        })
    )
