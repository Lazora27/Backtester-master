import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CVIRatio_WeightedPutCallRatio_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CVIRatio und WeightedPutCallRatio
    """
    
    params = (
        ('indicators', {
            'CVIRatio': {
                'class': CVIRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CVIRatio'>
            },
            'WeightedPutCallRatio': {
                'class': WeightedPutCallRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeightedPutCallRatio'>
            }
        }),
        ('weights', {
            'CVIRatio': 1.0,
            'WeightedPutCallRatio': 1.0
        })
    )
