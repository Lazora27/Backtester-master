import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StandardDeviationIndicator_FlowOfFunds_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StandardDeviationIndicator und FlowOfFunds
    """
    
    params = (
        ('indicators', {
            'StandardDeviationIndicator': {
                'class': StandardDeviationIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StandardDeviationIndicator'>
            },
            'FlowOfFunds': {
                'class': FlowOfFunds,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FlowOfFunds'>
            }
        }),
        ('weights', {
            'StandardDeviationIndicator': 1.0,
            'FlowOfFunds': 1.0
        })
    )
