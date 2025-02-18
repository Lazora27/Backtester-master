import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ParabolicSAR_FisherSignals_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ParabolicSAR und FisherSignals
    """
    
    params = (
        ('indicators', {
            'ParabolicSAR': {
                'class': ParabolicSAR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ParabolicSAR'>
            },
            'FisherSignals': {
                'class': FisherSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FisherSignals'>
            }
        }),
        ('weights', {
            'ParabolicSAR': 1.0,
            'FisherSignals': 1.0
        })
    )
