import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FisherTransform_CCITurbo_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FisherTransform und CCITurbo
    """
    
    params = (
        ('indicators', {
            'FisherTransform': {
                'class': FisherTransform,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FisherTransform'>
            },
            'CCITurbo': {
                'class': CCITurbo,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CCITurbo'>
            }
        }),
        ('weights', {
            'FisherTransform': 1.0,
            'CCITurbo': 1.0
        })
    )
