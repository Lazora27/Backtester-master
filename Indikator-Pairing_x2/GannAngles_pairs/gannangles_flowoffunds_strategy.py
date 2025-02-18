import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannAngles_FlowOfFunds_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannAngles und FlowOfFunds
    """
    
    params = (
        ('indicators', {
            'GannAngles': {
                'class': GannAngles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannAngles1'>
            },
            'FlowOfFunds': {
                'class': FlowOfFunds,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FlowOfFunds'>
            }
        }),
        ('weights', {
            'GannAngles': 1.0,
            'FlowOfFunds': 1.0
        })
    )
