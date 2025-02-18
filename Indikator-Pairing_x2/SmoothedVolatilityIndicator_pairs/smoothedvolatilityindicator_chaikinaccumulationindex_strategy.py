import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SmoothedVolatilityIndicator_ChaikinAccumulationIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SmoothedVolatilityIndicator und ChaikinAccumulationIndex
    """
    
    params = (
        ('indicators', {
            'SmoothedVolatilityIndicator': {
                'class': SmoothedVolatilityIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmoothedVolatilityIndicator'>
            },
            'ChaikinAccumulationIndex': {
                'class': ChaikinAccumulationIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChaikinAccumulationIndex'>
            }
        }),
        ('weights', {
            'SmoothedVolatilityIndicator': 1.0,
            'ChaikinAccumulationIndex': 1.0
        })
    )
