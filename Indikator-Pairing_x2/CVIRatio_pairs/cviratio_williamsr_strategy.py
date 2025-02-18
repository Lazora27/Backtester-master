import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CVIRatio_WilliamsR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CVIRatio und WilliamsR
    """
    
    params = (
        ('indicators', {
            'CVIRatio': {
                'class': CVIRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CVIRatio'>
            },
            'WilliamsR': {
                'class': WilliamsR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WilliamsR1'>
            }
        }),
        ('weights', {
            'CVIRatio': 1.0,
            'WilliamsR': 1.0
        })
    )
