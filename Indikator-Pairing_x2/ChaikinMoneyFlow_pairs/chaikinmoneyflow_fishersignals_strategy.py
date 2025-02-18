import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ChaikinMoneyFlow_FisherSignals_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ChaikinMoneyFlow und FisherSignals
    """
    
    params = (
        ('indicators', {
            'ChaikinMoneyFlow': {
                'class': ChaikinMoneyFlow,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChaikinMoneyFlow'>
            },
            'FisherSignals': {
                'class': FisherSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FisherSignals'>
            }
        }),
        ('weights', {
            'ChaikinMoneyFlow': 1.0,
            'FisherSignals': 1.0
        })
    )
