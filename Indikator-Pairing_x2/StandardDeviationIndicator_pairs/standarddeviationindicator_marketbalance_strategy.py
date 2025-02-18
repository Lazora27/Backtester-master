import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StandardDeviationIndicator_MarketBalance_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StandardDeviationIndicator und MarketBalance
    """
    
    params = (
        ('indicators', {
            'StandardDeviationIndicator': {
                'class': StandardDeviationIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StandardDeviationIndicator'>
            },
            'MarketBalance': {
                'class': MarketBalance,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketBalance'>
            }
        }),
        ('weights', {
            'StandardDeviationIndicator': 1.0,
            'MarketBalance': 1.0
        })
    )
