import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ATRTrailingStopIndicator_LaggingVolatilityIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ATRTrailingStopIndicator und LaggingVolatilityIndex
    """
    
    params = (
        ('indicators', {
            'ATRTrailingStopIndicator': {
                'class': ATRTrailingStopIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ATRTrailingStopIndicator'>
            },
            'LaggingVolatilityIndex': {
                'class': LaggingVolatilityIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LaggingVolatilityIndex'>
            }
        }),
        ('weights', {
            'ATRTrailingStopIndicator': 1.0,
            'LaggingVolatilityIndex': 1.0
        })
    )
