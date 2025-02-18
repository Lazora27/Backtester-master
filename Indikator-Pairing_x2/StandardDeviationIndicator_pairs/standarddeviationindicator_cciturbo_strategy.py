import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StandardDeviationIndicator_CCITurbo_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StandardDeviationIndicator und CCITurbo
    """
    
    params = (
        ('indicators', {
            'StandardDeviationIndicator': {
                'class': StandardDeviationIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StandardDeviationIndicator'>
            },
            'CCITurbo': {
                'class': CCITurbo,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CCITurbo'>
            }
        }),
        ('weights', {
            'StandardDeviationIndicator': 1.0,
            'CCITurbo': 1.0
        })
    )
