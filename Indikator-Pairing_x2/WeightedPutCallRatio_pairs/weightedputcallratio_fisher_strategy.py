import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WeightedPutCallRatio_Fisher_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WeightedPutCallRatio und Fisher
    """
    
    params = (
        ('indicators', {
            'WeightedPutCallRatio': {
                'class': WeightedPutCallRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeightedPutCallRatio'>
            },
            'Fisher': {
                'class': Fisher,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_Fisher'>
            }
        }),
        ('weights', {
            'WeightedPutCallRatio': 1.0,
            'Fisher': 1.0
        })
    )
