import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RSIDivergence_CCITurbo_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RSIDivergence und CCITurbo
    """
    
    params = (
        ('indicators', {
            'RSIDivergence': {
                'class': RSIDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RSIDivergence'>
            },
            'CCITurbo': {
                'class': CCITurbo,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CCITurbo'>
            }
        }),
        ('weights', {
            'RSIDivergence': 1.0,
            'CCITurbo': 1.0
        })
    )
