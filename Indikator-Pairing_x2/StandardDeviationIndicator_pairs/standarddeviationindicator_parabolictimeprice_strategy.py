import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StandardDeviationIndicator_ParabolicTimePrice_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StandardDeviationIndicator und ParabolicTimePrice
    """
    
    params = (
        ('indicators', {
            'StandardDeviationIndicator': {
                'class': StandardDeviationIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StandardDeviationIndicator'>
            },
            'ParabolicTimePrice': {
                'class': ParabolicTimePrice,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ParabolicTimePrice'>
            }
        }),
        ('weights', {
            'StandardDeviationIndicator': 1.0,
            'ParabolicTimePrice': 1.0
        })
    )
