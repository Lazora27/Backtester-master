import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CVIRatio_TrueRange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CVIRatio und TrueRange
    """
    
    params = (
        ('indicators', {
            'CVIRatio': {
                'class': CVIRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CVIRatio'>
            },
            'TrueRange': {
                'class': TrueRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrueRange1'>
            }
        }),
        ('weights', {
            'CVIRatio': 1.0,
            'TrueRange': 1.0
        })
    )
