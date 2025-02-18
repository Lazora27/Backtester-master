import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ModifiedATR_FisherSignals_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ModifiedATR und FisherSignals
    """
    
    params = (
        ('indicators', {
            'ModifiedATR': {
                'class': ModifiedATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ModifiedATR'>
            },
            'FisherSignals': {
                'class': FisherSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FisherSignals'>
            }
        }),
        ('weights', {
            'ModifiedATR': 1.0,
            'FisherSignals': 1.0
        })
    )
