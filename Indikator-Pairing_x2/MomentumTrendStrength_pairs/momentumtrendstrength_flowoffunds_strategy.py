import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MomentumTrendStrength_FlowOfFunds_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MomentumTrendStrength und FlowOfFunds
    """
    
    params = (
        ('indicators', {
            'MomentumTrendStrength': {
                'class': MomentumTrendStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MomentumTrendStrength'>
            },
            'FlowOfFunds': {
                'class': FlowOfFunds,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FlowOfFunds'>
            }
        }),
        ('weights', {
            'MomentumTrendStrength': 1.0,
            'FlowOfFunds': 1.0
        })
    )
