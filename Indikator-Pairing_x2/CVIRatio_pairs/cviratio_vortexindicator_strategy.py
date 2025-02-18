import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CVIRatio_VortexIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CVIRatio und VortexIndicator
    """
    
    params = (
        ('indicators', {
            'CVIRatio': {
                'class': CVIRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CVIRatio'>
            },
            'VortexIndicator': {
                'class': VortexIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VortexIndicator'>
            }
        }),
        ('weights', {
            'CVIRatio': 1.0,
            'VortexIndicator': 1.0
        })
    )
