import backtrader as bt
from ..base_strategy import FlexibleStrategy

class EhlersFisherTransform_TimeCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von EhlersFisherTransform und TimeCycle
    """
    
    params = (
        ('indicators', {
            'EhlersFisherTransform': {
                'class': EhlersFisherTransform,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EhlersFisherTransform'>
            },
            'TimeCycle': {
                'class': TimeCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeCycle'>
            }
        }),
        ('weights', {
            'EhlersFisherTransform': 1.0,
            'TimeCycle': 1.0
        })
    )
