import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SmartOrderBlock_FisherSignals_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SmartOrderBlock und FisherSignals
    """
    
    params = (
        ('indicators', {
            'SmartOrderBlock': {
                'class': SmartOrderBlock,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmartOrderBlock'>
            },
            'FisherSignals': {
                'class': FisherSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FisherSignals'>
            }
        }),
        ('weights', {
            'SmartOrderBlock': 1.0,
            'FisherSignals': 1.0
        })
    )
