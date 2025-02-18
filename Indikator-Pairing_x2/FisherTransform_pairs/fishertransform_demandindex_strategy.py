import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FisherTransform_DemandIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FisherTransform und DemandIndex
    """
    
    params = (
        ('indicators', {
            'FisherTransform': {
                'class': FisherTransform,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FisherTransform'>
            },
            'DemandIndex': {
                'class': DemandIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DemandIndex'>
            }
        }),
        ('weights', {
            'FisherTransform': 1.0,
            'DemandIndex': 1.0
        })
    )
