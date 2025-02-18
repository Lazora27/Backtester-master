import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AutoFibonacci_FisherSignals_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AutoFibonacci und FisherSignals
    """
    
    params = (
        ('indicators', {
            'AutoFibonacci': {
                'class': AutoFibonacci,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AutoFibonacci'>
            },
            'FisherSignals': {
                'class': FisherSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FisherSignals'>
            }
        }),
        ('weights', {
            'AutoFibonacci': 1.0,
            'FisherSignals': 1.0
        })
    )
