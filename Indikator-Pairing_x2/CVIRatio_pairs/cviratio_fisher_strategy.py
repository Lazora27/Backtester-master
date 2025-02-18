import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CVIRatio_Fisher_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CVIRatio und Fisher
    """
    
    params = (
        ('indicators', {
            'CVIRatio': {
                'class': CVIRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CVIRatio'>
            },
            'Fisher': {
                'class': Fisher,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_Fisher'>
            }
        }),
        ('weights', {
            'CVIRatio': 1.0,
            'Fisher': 1.0
        })
    )
