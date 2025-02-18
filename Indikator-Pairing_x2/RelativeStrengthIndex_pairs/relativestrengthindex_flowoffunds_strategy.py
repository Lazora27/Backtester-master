import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RelativeStrengthIndex_FlowOfFunds_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RelativeStrengthIndex und FlowOfFunds
    """
    
    params = (
        ('indicators', {
            'RelativeStrengthIndex': {
                'class': RelativeStrengthIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RelativeStrengthIndex1'>
            },
            'FlowOfFunds': {
                'class': FlowOfFunds,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FlowOfFunds'>
            }
        }),
        ('weights', {
            'RelativeStrengthIndex': 1.0,
            'FlowOfFunds': 1.0
        })
    )
