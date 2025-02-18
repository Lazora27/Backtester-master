import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TrueRange_AdaptiveATR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TrueRange und AdaptiveATR
    """
    
    params = (
        ('indicators', {
            'TrueRange': {
                'class': TrueRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrueRange1'>
            },
            'AdaptiveATR': {
                'class': AdaptiveATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveATR'>
            }
        }),
        ('weights', {
            'TrueRange': 1.0,
            'AdaptiveATR': 1.0
        })
    )
