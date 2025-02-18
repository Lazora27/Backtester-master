import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FisherTransform_TimeCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FisherTransform und TimeCycle
    """
    
    params = (
        ('indicators', {
            'FisherTransform': {
                'class': FisherTransform,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FisherTransform'>
            },
            'TimeCycle': {
                'class': TimeCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeCycle'>
            }
        }),
        ('weights', {
            'FisherTransform': 1.0,
            'TimeCycle': 1.0
        })
    )
