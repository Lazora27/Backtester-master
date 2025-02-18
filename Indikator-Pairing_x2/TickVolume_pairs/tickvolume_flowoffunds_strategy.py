import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TickVolume_FlowOfFunds_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TickVolume und FlowOfFunds
    """
    
    params = (
        ('indicators', {
            'TickVolume': {
                'class': TickVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickVolume'>
            },
            'FlowOfFunds': {
                'class': FlowOfFunds,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FlowOfFunds'>
            }
        }),
        ('weights', {
            'TickVolume': 1.0,
            'FlowOfFunds': 1.0
        })
    )
