import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RelativeVolatilityIndex_TRIXIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RelativeVolatilityIndex und TRIXIndicator
    """
    
    params = (
        ('indicators', {
            'RelativeVolatilityIndex': {
                'class': RelativeVolatilityIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RelativeVolatilityIndex'>
            },
            'TRIXIndicator': {
                'class': TRIXIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TRIXIndicator'>
            }
        }),
        ('weights', {
            'RelativeVolatilityIndex': 1.0,
            'TRIXIndicator': 1.0
        })
    )
