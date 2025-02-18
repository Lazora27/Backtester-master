import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WeightedPutCallRatio_EldersForceIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WeightedPutCallRatio und EldersForceIndex
    """
    
    params = (
        ('indicators', {
            'WeightedPutCallRatio': {
                'class': WeightedPutCallRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeightedPutCallRatio'>
            },
            'EldersForceIndex': {
                'class': EldersForceIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EldersForceIndex'>
            }
        }),
        ('weights', {
            'WeightedPutCallRatio': 1.0,
            'EldersForceIndex': 1.0
        })
    )
