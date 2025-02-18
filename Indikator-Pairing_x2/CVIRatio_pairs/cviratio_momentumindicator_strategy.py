import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CVIRatio_MomentumIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CVIRatio und MomentumIndicator
    """
    
    params = (
        ('indicators', {
            'CVIRatio': {
                'class': CVIRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CVIRatio'>
            },
            'MomentumIndicator': {
                'class': MomentumIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MomentumIndicator'>
            }
        }),
        ('weights', {
            'CVIRatio': 1.0,
            'MomentumIndicator': 1.0
        })
    )
