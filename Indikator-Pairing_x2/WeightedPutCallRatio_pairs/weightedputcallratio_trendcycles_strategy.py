import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WeightedPutCallRatio_TrendCycles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WeightedPutCallRatio und TrendCycles
    """
    
    params = (
        ('indicators', {
            'WeightedPutCallRatio': {
                'class': WeightedPutCallRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeightedPutCallRatio'>
            },
            'TrendCycles': {
                'class': TrendCycles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrendCycles'>
            }
        }),
        ('weights', {
            'WeightedPutCallRatio': 1.0,
            'TrendCycles': 1.0
        })
    )
