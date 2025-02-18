import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WeightedPutCallRatio_TrueRange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WeightedPutCallRatio und TrueRange
    """
    
    params = (
        ('indicators', {
            'WeightedPutCallRatio': {
                'class': WeightedPutCallRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeightedPutCallRatio'>
            },
            'TrueRange': {
                'class': TrueRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrueRange1'>
            }
        }),
        ('weights', {
            'WeightedPutCallRatio': 1.0,
            'TrueRange': 1.0
        })
    )
