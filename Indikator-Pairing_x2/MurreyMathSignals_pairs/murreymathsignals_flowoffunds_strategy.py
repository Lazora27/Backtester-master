import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MurreyMathSignals_FlowOfFunds_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MurreyMathSignals und FlowOfFunds
    """
    
    params = (
        ('indicators', {
            'MurreyMathSignals': {
                'class': MurreyMathSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MurreyMathSignals'>
            },
            'FlowOfFunds': {
                'class': FlowOfFunds,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FlowOfFunds'>
            }
        }),
        ('weights', {
            'MurreyMathSignals': 1.0,
            'FlowOfFunds': 1.0
        })
    )
