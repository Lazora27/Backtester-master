import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CVIRatio_AdvancedCandlePattern_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CVIRatio und AdvancedCandlePattern
    """
    
    params = (
        ('indicators', {
            'CVIRatio': {
                'class': CVIRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CVIRatio'>
            },
            'AdvancedCandlePattern': {
                'class': AdvancedCandlePattern,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdvancedCandlePattern'>
            }
        }),
        ('weights', {
            'CVIRatio': 1.0,
            'AdvancedCandlePattern': 1.0
        })
    )
