import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AwesomeOscillator_FlowOfFunds_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AwesomeOscillator und FlowOfFunds
    """
    
    params = (
        ('indicators', {
            'AwesomeOscillator': {
                'class': AwesomeOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AwesomeOscillator1'>
            },
            'FlowOfFunds': {
                'class': FlowOfFunds,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FlowOfFunds'>
            }
        }),
        ('weights', {
            'AwesomeOscillator': 1.0,
            'FlowOfFunds': 1.0
        })
    )
