import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CoppockCurve_MomentumTrendStrength_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CoppockCurve und MomentumTrendStrength
    """
    
    params = (
        ('indicators', {
            'CoppockCurve': {
                'class': CoppockCurve,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CoppockCurve'>
            },
            'MomentumTrendStrength': {
                'class': MomentumTrendStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MomentumTrendStrength'>
            }
        }),
        ('weights', {
            'CoppockCurve': 1.0,
            'MomentumTrendStrength': 1.0
        })
    )
