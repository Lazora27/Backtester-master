import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StandardDeviationIndicator_AccelerationBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StandardDeviationIndicator und AccelerationBands
    """
    
    params = (
        ('indicators', {
            'StandardDeviationIndicator': {
                'class': StandardDeviationIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StandardDeviationIndicator'>
            },
            'AccelerationBands': {
                'class': AccelerationBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AccelerationBands'>
            }
        }),
        ('weights', {
            'StandardDeviationIndicator': 1.0,
            'AccelerationBands': 1.0
        })
    )
