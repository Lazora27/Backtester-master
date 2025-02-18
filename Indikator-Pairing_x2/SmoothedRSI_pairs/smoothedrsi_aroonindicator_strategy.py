import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SmoothedRSI_AroonIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SmoothedRSI und AroonIndicator
    """
    
    params = (
        ('indicators', {
            'SmoothedRSI': {
                'class': SmoothedRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmoothedRSI'>
            },
            'AroonIndicator': {
                'class': AroonIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AroonIndicator'>
            }
        }),
        ('weights', {
            'SmoothedRSI': 1.0,
            'AroonIndicator': 1.0
        })
    )
