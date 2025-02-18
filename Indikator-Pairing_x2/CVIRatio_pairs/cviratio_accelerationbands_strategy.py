import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CVIRatio_AccelerationBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CVIRatio und AccelerationBands
    """
    
    params = (
        ('indicators', {
            'CVIRatio': {
                'class': CVIRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CVIRatio'>
            },
            'AccelerationBands': {
                'class': AccelerationBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AccelerationBands'>
            }
        }),
        ('weights', {
            'CVIRatio': 1.0,
            'AccelerationBands': 1.0
        })
    )
