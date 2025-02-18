import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BarStrength_FlowOfFunds_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BarStrength und FlowOfFunds
    """
    
    params = (
        ('indicators', {
            'BarStrength': {
                'class': BarStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BarStrength'>
            },
            'FlowOfFunds': {
                'class': FlowOfFunds,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FlowOfFunds'>
            }
        }),
        ('weights', {
            'BarStrength': 1.0,
            'FlowOfFunds': 1.0
        })
    )
