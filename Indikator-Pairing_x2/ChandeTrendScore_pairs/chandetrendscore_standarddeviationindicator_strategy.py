import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ChandeTrendScore_StandardDeviationIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ChandeTrendScore und StandardDeviationIndicator
    """
    
    params = (
        ('indicators', {
            'ChandeTrendScore': {
                'class': ChandeTrendScore,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChandeTrendScore'>
            },
            'StandardDeviationIndicator': {
                'class': StandardDeviationIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StandardDeviationIndicator'>
            }
        }),
        ('weights', {
            'ChandeTrendScore': 1.0,
            'StandardDeviationIndicator': 1.0
        })
    )
