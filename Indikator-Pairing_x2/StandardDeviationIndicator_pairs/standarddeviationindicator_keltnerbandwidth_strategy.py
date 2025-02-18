import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StandardDeviationIndicator_KeltnerBandWidth_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StandardDeviationIndicator und KeltnerBandWidth
    """
    
    params = (
        ('indicators', {
            'StandardDeviationIndicator': {
                'class': StandardDeviationIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StandardDeviationIndicator'>
            },
            'KeltnerBandWidth': {
                'class': KeltnerBandWidth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KeltnerBandWidth'>
            }
        }),
        ('weights', {
            'StandardDeviationIndicator': 1.0,
            'KeltnerBandWidth': 1.0
        })
    )
