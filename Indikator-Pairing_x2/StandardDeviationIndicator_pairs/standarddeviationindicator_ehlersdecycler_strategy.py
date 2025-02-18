import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StandardDeviationIndicator_EhlersDecycler_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StandardDeviationIndicator und EhlersDecycler
    """
    
    params = (
        ('indicators', {
            'StandardDeviationIndicator': {
                'class': StandardDeviationIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StandardDeviationIndicator'>
            },
            'EhlersDecycler': {
                'class': EhlersDecycler,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EhlersDecycler'>
            }
        }),
        ('weights', {
            'StandardDeviationIndicator': 1.0,
            'EhlersDecycler': 1.0
        })
    )
