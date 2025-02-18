import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FisherTransform_CyberCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FisherTransform und CyberCycle
    """
    
    params = (
        ('indicators', {
            'FisherTransform': {
                'class': FisherTransform,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FisherTransform'>
            },
            'CyberCycle': {
                'class': CyberCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CyberCycle'>
            }
        }),
        ('weights', {
            'FisherTransform': 1.0,
            'CyberCycle': 1.0
        })
    )
