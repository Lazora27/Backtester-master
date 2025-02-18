import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CVIRatio_TrendCycles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CVIRatio und TrendCycles
    """
    
    params = (
        ('indicators', {
            'CVIRatio': {
                'class': CVIRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CVIRatio'>
            },
            'TrendCycles': {
                'class': TrendCycles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrendCycles'>
            }
        }),
        ('weights', {
            'CVIRatio': 1.0,
            'TrendCycles': 1.0
        })
    )
