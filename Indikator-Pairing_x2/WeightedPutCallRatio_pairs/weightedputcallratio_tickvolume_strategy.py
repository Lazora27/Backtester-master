import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WeightedPutCallRatio_TickVolume_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WeightedPutCallRatio und TickVolume
    """
    
    params = (
        ('indicators', {
            'WeightedPutCallRatio': {
                'class': WeightedPutCallRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeightedPutCallRatio'>
            },
            'TickVolume': {
                'class': TickVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickVolume'>
            }
        }),
        ('weights', {
            'WeightedPutCallRatio': 1.0,
            'TickVolume': 1.0
        })
    )
