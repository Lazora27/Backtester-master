import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SmoothedRSI_VolatilityIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SmoothedRSI und VolatilityIndex
    """
    
    params = (
        ('indicators', {
            'SmoothedRSI': {
                'class': SmoothedRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmoothedRSI'>
            },
            'VolatilityIndex': {
                'class': VolatilityIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolatilityIndex'>
            }
        }),
        ('weights', {
            'SmoothedRSI': 1.0,
            'VolatilityIndex': 1.0
        })
    )
