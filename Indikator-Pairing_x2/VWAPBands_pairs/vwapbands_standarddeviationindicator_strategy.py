import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VWAPBands_StandardDeviationIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VWAPBands und StandardDeviationIndicator
    """
    
    params = (
        ('indicators', {
            'VWAPBands': {
                'class': VWAPBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VWAPBands'>
            },
            'StandardDeviationIndicator': {
                'class': StandardDeviationIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StandardDeviationIndicator'>
            }
        }),
        ('weights', {
            'VWAPBands': 1.0,
            'StandardDeviationIndicator': 1.0
        })
    )
