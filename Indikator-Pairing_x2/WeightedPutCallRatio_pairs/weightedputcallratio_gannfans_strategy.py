import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WeightedPutCallRatio_GannFans_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WeightedPutCallRatio und GannFans
    """
    
    params = (
        ('indicators', {
            'WeightedPutCallRatio': {
                'class': WeightedPutCallRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeightedPutCallRatio'>
            },
            'GannFans': {
                'class': GannFans,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannFans'>
            }
        }),
        ('weights', {
            'WeightedPutCallRatio': 1.0,
            'GannFans': 1.0
        })
    )
