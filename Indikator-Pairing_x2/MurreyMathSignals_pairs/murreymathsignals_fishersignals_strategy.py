import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MurreyMathSignals_FisherSignals_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MurreyMathSignals und FisherSignals
    """
    
    params = (
        ('indicators', {
            'MurreyMathSignals': {
                'class': MurreyMathSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MurreyMathSignals'>
            },
            'FisherSignals': {
                'class': FisherSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FisherSignals'>
            }
        }),
        ('weights', {
            'MurreyMathSignals': 1.0,
            'FisherSignals': 1.0
        })
    )
