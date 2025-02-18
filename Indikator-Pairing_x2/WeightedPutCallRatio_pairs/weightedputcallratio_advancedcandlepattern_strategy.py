import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WeightedPutCallRatio_AdvancedCandlePattern_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WeightedPutCallRatio und AdvancedCandlePattern
    """
    
    params = (
        ('indicators', {
            'WeightedPutCallRatio': {
                'class': WeightedPutCallRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeightedPutCallRatio'>
            },
            'AdvancedCandlePattern': {
                'class': AdvancedCandlePattern,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdvancedCandlePattern'>
            }
        }),
        ('weights', {
            'WeightedPutCallRatio': 1.0,
            'AdvancedCandlePattern': 1.0
        })
    )
