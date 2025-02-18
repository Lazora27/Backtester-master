import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FisherTransform_MassIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FisherTransform und MassIndex
    """
    
    params = (
        ('indicators', {
            'FisherTransform': {
                'class': FisherTransform,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FisherTransform'>
            },
            'MassIndex': {
                'class': MassIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MassIndex'>
            }
        }),
        ('weights', {
            'FisherTransform': 1.0,
            'MassIndex': 1.0
        })
    )
