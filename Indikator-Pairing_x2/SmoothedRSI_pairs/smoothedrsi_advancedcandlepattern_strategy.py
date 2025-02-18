import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SmoothedRSI_AdvancedCandlePattern_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SmoothedRSI und AdvancedCandlePattern
    """
    
    params = (
        ('indicators', {
            'SmoothedRSI': {
                'class': SmoothedRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmoothedRSI'>
            },
            'AdvancedCandlePattern': {
                'class': AdvancedCandlePattern,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdvancedCandlePattern'>
            }
        }),
        ('weights', {
            'SmoothedRSI': 1.0,
            'AdvancedCandlePattern': 1.0
        })
    )
