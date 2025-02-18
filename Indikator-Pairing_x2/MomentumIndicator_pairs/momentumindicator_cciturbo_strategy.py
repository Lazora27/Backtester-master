import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MomentumIndicator_CCITurbo_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MomentumIndicator und CCITurbo
    """
    
    params = (
        ('indicators', {
            'MomentumIndicator': {
                'class': MomentumIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MomentumIndicator'>
            },
            'CCITurbo': {
                'class': CCITurbo,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CCITurbo'>
            }
        }),
        ('weights', {
            'MomentumIndicator': 1.0,
            'CCITurbo': 1.0
        })
    )
