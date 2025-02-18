import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SmoothedRSI_TrendCycles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SmoothedRSI und TrendCycles
    """
    
    params = (
        ('indicators', {
            'SmoothedRSI': {
                'class': SmoothedRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmoothedRSI'>
            },
            'TrendCycles': {
                'class': TrendCycles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrendCycles'>
            }
        }),
        ('weights', {
            'SmoothedRSI': 1.0,
            'TrendCycles': 1.0
        })
    )
