import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CVIRatio_FourierCycleFilter_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CVIRatio und FourierCycleFilter
    """
    
    params = (
        ('indicators', {
            'CVIRatio': {
                'class': CVIRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CVIRatio'>
            },
            'FourierCycleFilter': {
                'class': FourierCycleFilter,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FourierCycleFilter'>
            }
        }),
        ('weights', {
            'CVIRatio': 1.0,
            'FourierCycleFilter': 1.0
        })
    )
