import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PriceSquawk_StandardDeviationIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PriceSquawk und StandardDeviationIndicator
    """
    
    params = (
        ('indicators', {
            'PriceSquawk': {
                'class': PriceSquawk,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceSquawk'>
            },
            'StandardDeviationIndicator': {
                'class': StandardDeviationIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StandardDeviationIndicator'>
            }
        }),
        ('weights', {
            'PriceSquawk': 1.0,
            'StandardDeviationIndicator': 1.0
        })
    )
