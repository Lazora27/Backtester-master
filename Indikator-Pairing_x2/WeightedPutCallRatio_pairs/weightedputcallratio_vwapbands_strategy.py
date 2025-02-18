import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WeightedPutCallRatio_VWAPBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WeightedPutCallRatio und VWAPBands
    """
    
    params = (
        ('indicators', {
            'WeightedPutCallRatio': {
                'class': WeightedPutCallRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeightedPutCallRatio'>
            },
            'VWAPBands': {
                'class': VWAPBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VWAPBands'>
            }
        }),
        ('weights', {
            'WeightedPutCallRatio': 1.0,
            'VWAPBands': 1.0
        })
    )
