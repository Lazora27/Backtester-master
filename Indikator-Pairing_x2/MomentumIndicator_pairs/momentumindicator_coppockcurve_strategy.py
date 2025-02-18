import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MomentumIndicator_CoppockCurve_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MomentumIndicator und CoppockCurve
    """
    
    params = (
        ('indicators', {
            'MomentumIndicator': {
                'class': MomentumIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MomentumIndicator'>
            },
            'CoppockCurve': {
                'class': CoppockCurve,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CoppockCurve'>
            }
        }),
        ('weights', {
            'MomentumIndicator': 1.0,
            'CoppockCurve': 1.0
        })
    )
