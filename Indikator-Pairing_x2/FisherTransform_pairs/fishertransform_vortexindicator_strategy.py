import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FisherTransform_VortexIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FisherTransform und VortexIndicator
    """
    
    params = (
        ('indicators', {
            'FisherTransform': {
                'class': FisherTransform,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FisherTransform'>
            },
            'VortexIndicator': {
                'class': VortexIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VortexIndicator'>
            }
        }),
        ('weights', {
            'FisherTransform': 1.0,
            'VortexIndicator': 1.0
        })
    )
