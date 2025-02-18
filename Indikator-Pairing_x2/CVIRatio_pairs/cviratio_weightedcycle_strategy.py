import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CVIRatio_WeightedCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CVIRatio und WeightedCycle
    """
    
    params = (
        ('indicators', {
            'CVIRatio': {
                'class': CVIRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CVIRatio'>
            },
            'WeightedCycle': {
                'class': WeightedCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeightedCycle'>
            }
        }),
        ('weights', {
            'CVIRatio': 1.0,
            'WeightedCycle': 1.0
        })
    )
