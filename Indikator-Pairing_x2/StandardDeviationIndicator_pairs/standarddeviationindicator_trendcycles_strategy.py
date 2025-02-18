import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StandardDeviationIndicator_TrendCycles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StandardDeviationIndicator und TrendCycles
    """
    
    params = (
        ('indicators', {
            'StandardDeviationIndicator': {
                'class': StandardDeviationIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StandardDeviationIndicator'>
            },
            'TrendCycles': {
                'class': TrendCycles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrendCycles'>
            }
        }),
        ('weights', {
            'StandardDeviationIndicator': 1.0,
            'TrendCycles': 1.0
        })
    )
