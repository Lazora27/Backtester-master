import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WeightedPutCallRatio_IchimokuCloud_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WeightedPutCallRatio und IchimokuCloud
    """
    
    params = (
        ('indicators', {
            'WeightedPutCallRatio': {
                'class': WeightedPutCallRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeightedPutCallRatio'>
            },
            'IchimokuCloud': {
                'class': IchimokuCloud,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_IchimokuCloud'>
            }
        }),
        ('weights', {
            'WeightedPutCallRatio': 1.0,
            'IchimokuCloud': 1.0
        })
    )
