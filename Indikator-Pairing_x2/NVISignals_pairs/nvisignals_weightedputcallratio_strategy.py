import backtrader as bt
from ..base_strategy import FlexibleStrategy

class NVISignals_WeightedPutCallRatio_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von NVISignals und WeightedPutCallRatio
    """
    
    params = (
        ('indicators', {
            'NVISignals': {
                'class': NVISignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_NVISignals'>
            },
            'WeightedPutCallRatio': {
                'class': WeightedPutCallRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeightedPutCallRatio'>
            }
        }),
        ('weights', {
            'NVISignals': 1.0,
            'WeightedPutCallRatio': 1.0
        })
    )
