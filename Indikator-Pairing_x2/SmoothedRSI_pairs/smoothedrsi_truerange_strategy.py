import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SmoothedRSI_TrueRange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SmoothedRSI und TrueRange
    """
    
    params = (
        ('indicators', {
            'SmoothedRSI': {
                'class': SmoothedRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmoothedRSI'>
            },
            'TrueRange': {
                'class': TrueRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrueRange1'>
            }
        }),
        ('weights', {
            'SmoothedRSI': 1.0,
            'TrueRange': 1.0
        })
    )
