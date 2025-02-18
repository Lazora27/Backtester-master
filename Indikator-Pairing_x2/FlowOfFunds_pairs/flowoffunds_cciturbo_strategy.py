import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FlowOfFunds_CCITurbo_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FlowOfFunds und CCITurbo
    """
    
    params = (
        ('indicators', {
            'FlowOfFunds': {
                'class': FlowOfFunds,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FlowOfFunds'>
            },
            'CCITurbo': {
                'class': CCITurbo,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CCITurbo'>
            }
        }),
        ('weights', {
            'FlowOfFunds': 1.0,
            'CCITurbo': 1.0
        })
    )
