import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CVIRatio_MomentumTrendStrength_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CVIRatio und MomentumTrendStrength
    """
    
    params = (
        ('indicators', {
            'CVIRatio': {
                'class': CVIRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CVIRatio'>
            },
            'MomentumTrendStrength': {
                'class': MomentumTrendStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MomentumTrendStrength'>
            }
        }),
        ('weights', {
            'CVIRatio': 1.0,
            'MomentumTrendStrength': 1.0
        })
    )
