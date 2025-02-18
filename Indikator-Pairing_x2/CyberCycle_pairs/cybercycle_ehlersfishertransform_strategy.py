import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CyberCycle_EhlersFisherTransform_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CyberCycle und EhlersFisherTransform
    """
    
    params = (
        ('indicators', {
            'CyberCycle': {
                'class': CyberCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CyberCycle'>
            },
            'EhlersFisherTransform': {
                'class': EhlersFisherTransform,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EhlersFisherTransform'>
            }
        }),
        ('weights', {
            'CyberCycle': 1.0,
            'EhlersFisherTransform': 1.0
        })
    )
