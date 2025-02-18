import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ArmsIndex_FlowOfFunds_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ArmsIndex und FlowOfFunds
    """
    
    params = (
        ('indicators', {
            'ArmsIndex': {
                'class': ArmsIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ArmsIndex'>
            },
            'FlowOfFunds': {
                'class': FlowOfFunds,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FlowOfFunds'>
            }
        }),
        ('weights', {
            'ArmsIndex': 1.0,
            'FlowOfFunds': 1.0
        })
    )
