import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CVIRatio_VolatilityIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CVIRatio und VolatilityIndex
    """
    
    params = (
        ('indicators', {
            'CVIRatio': {
                'class': CVIRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CVIRatio'>
            },
            'VolatilityIndex': {
                'class': VolatilityIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolatilityIndex'>
            }
        }),
        ('weights', {
            'CVIRatio': 1.0,
            'VolatilityIndex': 1.0
        })
    )
