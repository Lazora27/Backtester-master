import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StandardDeviationIndicator_DPOCycles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StandardDeviationIndicator und DPOCycles
    """
    
    params = (
        ('indicators', {
            'StandardDeviationIndicator': {
                'class': StandardDeviationIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StandardDeviationIndicator'>
            },
            'DPOCycles': {
                'class': DPOCycles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DPOCycles'>
            }
        }),
        ('weights', {
            'StandardDeviationIndicator': 1.0,
            'DPOCycles': 1.0
        })
    )
