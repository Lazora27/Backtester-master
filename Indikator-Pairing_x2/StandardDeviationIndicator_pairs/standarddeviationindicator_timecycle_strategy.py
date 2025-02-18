import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StandardDeviationIndicator_TimeCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StandardDeviationIndicator und TimeCycle
    """
    
    params = (
        ('indicators', {
            'StandardDeviationIndicator': {
                'class': StandardDeviationIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StandardDeviationIndicator'>
            },
            'TimeCycle': {
                'class': TimeCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeCycle'>
            }
        }),
        ('weights', {
            'StandardDeviationIndicator': 1.0,
            'TimeCycle': 1.0
        })
    )
