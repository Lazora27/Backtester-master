import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MoneyFlowIndex_FisherSignals_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MoneyFlowIndex und FisherSignals
    """
    
    params = (
        ('indicators', {
            'MoneyFlowIndex': {
                'class': MoneyFlowIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MoneyFlowIndex'>
            },
            'FisherSignals': {
                'class': FisherSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FisherSignals'>
            }
        }),
        ('weights', {
            'MoneyFlowIndex': 1.0,
            'FisherSignals': 1.0
        })
    )
