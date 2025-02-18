import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CVIRatio_AndrewsPitchfork_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CVIRatio und AndrewsPitchfork
    """
    
    params = (
        ('indicators', {
            'CVIRatio': {
                'class': CVIRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CVIRatio'>
            },
            'AndrewsPitchfork': {
                'class': AndrewsPitchfork,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AndrewsPitchfork'>
            }
        }),
        ('weights', {
            'CVIRatio': 1.0,
            'AndrewsPitchfork': 1.0
        })
    )
