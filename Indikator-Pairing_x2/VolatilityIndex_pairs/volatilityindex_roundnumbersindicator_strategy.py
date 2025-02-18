import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VolatilityIndex_RoundNumbersIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VolatilityIndex und RoundNumbersIndicator
    """
    
    params = (
        ('indicators', {
            'VolatilityIndex': {
                'class': VolatilityIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolatilityIndex'>
            },
            'RoundNumbersIndicator': {
                'class': RoundNumbersIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RoundNumbersIndicator'>
            }
        }),
        ('weights', {
            'VolatilityIndex': 1.0,
            'RoundNumbersIndicator': 1.0
        })
    )
