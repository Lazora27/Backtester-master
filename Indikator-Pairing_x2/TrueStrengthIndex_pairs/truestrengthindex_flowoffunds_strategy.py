import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TrueStrengthIndex_FlowOfFunds_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TrueStrengthIndex und FlowOfFunds
    """
    
    params = (
        ('indicators', {
            'TrueStrengthIndex': {
                'class': TrueStrengthIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrueStrengthIndex'>
            },
            'FlowOfFunds': {
                'class': FlowOfFunds,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FlowOfFunds'>
            }
        }),
        ('weights', {
            'TrueStrengthIndex': 1.0,
            'FlowOfFunds': 1.0
        })
    )
