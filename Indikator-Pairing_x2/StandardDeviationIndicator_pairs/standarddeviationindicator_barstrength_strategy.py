import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StandardDeviationIndicator_BarStrength_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StandardDeviationIndicator und BarStrength
    """
    
    params = (
        ('indicators', {
            'StandardDeviationIndicator': {
                'class': StandardDeviationIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StandardDeviationIndicator'>
            },
            'BarStrength': {
                'class': BarStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BarStrength'>
            }
        }),
        ('weights', {
            'StandardDeviationIndicator': 1.0,
            'BarStrength': 1.0
        })
    )
