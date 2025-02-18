import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StandardDeviationIndicator_BuyingPressure_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StandardDeviationIndicator und BuyingPressure
    """
    
    params = (
        ('indicators', {
            'StandardDeviationIndicator': {
                'class': StandardDeviationIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StandardDeviationIndicator'>
            },
            'BuyingPressure': {
                'class': BuyingPressure,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BuyingPressure'>
            }
        }),
        ('weights', {
            'StandardDeviationIndicator': 1.0,
            'BuyingPressure': 1.0
        })
    )
