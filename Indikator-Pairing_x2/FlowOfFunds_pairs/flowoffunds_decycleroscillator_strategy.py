import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FlowOfFunds_DecyclerOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FlowOfFunds und DecyclerOscillator
    """
    
    params = (
        ('indicators', {
            'FlowOfFunds': {
                'class': FlowOfFunds,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FlowOfFunds'>
            },
            'DecyclerOscillator': {
                'class': DecyclerOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DecyclerOscillator'>
            }
        }),
        ('weights', {
            'FlowOfFunds': 1.0,
            'DecyclerOscillator': 1.0
        })
    )
