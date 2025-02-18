import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CCITurbo_EhlersFisherTransform_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CCITurbo und EhlersFisherTransform
    """
    
    params = (
        ('indicators', {
            'CCITurbo': {
                'class': CCITurbo,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CCITurbo'>
            },
            'EhlersFisherTransform': {
                'class': EhlersFisherTransform,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EhlersFisherTransform'>
            }
        }),
        ('weights', {
            'CCITurbo': 1.0,
            'EhlersFisherTransform': 1.0
        })
    )
