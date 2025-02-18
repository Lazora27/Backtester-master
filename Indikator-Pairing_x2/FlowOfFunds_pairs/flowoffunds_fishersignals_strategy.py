import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FlowOfFunds_FisherSignals_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FlowOfFunds und FisherSignals
    """
    
    params = (
        ('indicators', {
            'FlowOfFunds': {
                'class': FlowOfFunds,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FlowOfFunds'>
            },
            'FisherSignals': {
                'class': FisherSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FisherSignals'>
            }
        }),
        ('weights', {
            'FlowOfFunds': 1.0,
            'FisherSignals': 1.0
        })
    )
